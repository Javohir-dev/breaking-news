from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()
    context = {"news_list": news_list}

    return render(request, "news/news_list.html", context)


def detail_page(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    latest_news = News.published.all().order_by("-published_time")[:6]
    categories = Category.objects.all()
    first_letter = news.body[:1]
    news_body = news.body[1:]
    context = {
        "news": news,
        "latest_news": latest_news,
        "first_letter": first_letter,
        "categories": categories,
        "news_body": news_body,
    }

    return render(request, "news/single-post.html", context)


def homePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by("-published_time")[:5]
    local_news = News.objects.all().filter(category__name="Mahalliy")
    foreign_news = News.objects.all().filter(category__name="Xorijiy")
    numbers = 1
    context = {
        "news_list": news_list,
        "categories": categories,
        "numbers": numbers,
        "local_news": local_news,
        "foreign_news": foreign_news,
    }

    return render(request, "news/home.html", context)


class HomePageView(ListView):
    model = News
    template_name = "news/home.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.model.objects.all()
        context["news_list"] = News.published.all().order_by("-published_time")[:5]
        context["local_news"] = News.objects.all().filter(category__name="Mahalliy")
        context["foreign_news"] = News.objects.all().filter(category__name="Xorijiy")

        return context


class ContactPageView(TemplateView):
    template_name = "news/contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {"form": form}

        return render(request, "news/contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            # return HttpResponse("<h1>Thank you for message!</h1>")

        context = {"form": form}

        return render(request, "news/contact.html", context)


class ErrorPageView(TemplateView):
    template_name = "news/404-page.html"


def errorPageView(request):
    context = {}

    return render(request, "news/404-page.html", context)
