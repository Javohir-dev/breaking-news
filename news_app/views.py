from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()
    context = {"news_list": news_list}

    return render(request, "news/news_list.html", context)


class AboutView(ListView):
    model = News
    template_name = "news/about.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the News
        context["our_news"] = News.published.all().filter(category__name="about")

        return context


def detail_page(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    latest_news = News.published.all().order_by("-published_time")[:6]
    foreign_news = News.objects.all().filter(category__name="Xorijiy")
    local_news = News.objects.all().filter(category__name="Mahalliy")
    this_news = News.objects.all().filter(category__name=f"{news.category}")
    categories = Category.objects.all()
    first_letter = news.body[:1]
    news_body = news.body[1:]
    # Bu shartlar sahifadagi tavsiya bo'limidagi ma'lumotlar asosiy ko'rinib turgan ma'lumotlar bilan
    # bir-hil bo'lib qolmasligi uchun hizmat qilad.
    if news.category == foreign_news[0].category:
        second_news = News.objects.all().filter(category__name="Sport")
    else:
        second_news = News.objects.all().filter(category__name="Xorijiy")

    if news.category == local_news[0].category:
        third_news = News.objects.all().filter(category__name="Texno")
    else:
        third_news = News.objects.all().filter(category__name="Mahalliy")

    context = {
        "news": news,
        "latest_news": latest_news,
        "first_letter": first_letter,
        "categories": categories,
        "news_body": news_body,
        "this_news": this_news,
        "second_news": second_news,
        "second_news_category": second_news[0].category,
        "third_news": third_news,
        "third_news_category": third_news[0].category,
    }

    return render(request, "news/single-post.html", context)


# def homePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by("-published_time")[:5]
#     local_news = News.objects.all().filter(category__name="Mahalliy")
#     foreign_news = News.objects.all().filter(category__name="Xorijiy")
#     techno_news = News.objects.all().filter(category__name="Texno")
#     numbers = 1
#     context = {
#         "news_list": news_list,
#         "categories": categories,
#         "numbers": numbers,
#         "local_news": local_news,
#         "foreign_news": foreign_news,
#         "techno_news": techno_news,
#     }

#     return render(request, "news/home.html", context)


class HomePageView(ListView):
    model = News
    template_name = "news/home.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["top_five"] = (
            News.published.all()
            .order_by("-published_time")
            .filter(category__name="Texno")[:5]
        )
        context["news_list"] = News.published.all().order_by("-published_time")[5:]
        context["local_news"] = News.published.all().filter(category__name="Mahalliy")
        context["techno_news"] = News.published.all().filter(category__name="Texno")
        context["foreign_news"] = News.published.all().filter(category__name="Xorijiy")
        context["sport_news"] = News.published.all().filter(category__name="Sport")
        context["local_news_category"] = "Mahalliy"
        context["sport_news_category"] = "Sport"
        context["techno_news_category"] = "Texno"

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


class LocalNewsListView(ListView):
    model = News
    template_name = "news/local-news-list.html"
    context_object_name = "local_news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foreign_news"] = News.published.all().filter(category__name="Xorijiy")
        context["techno_news"] = News.published.all().filter(category__name="Texno")
        context["sport_news"] = News.published.all().filter(category__name="Sport")
        context["categories"] = Category.objects.all()
        context["local_news_category"] = "Mahalliy"
        context["sport_news_category"] = "Sport"
        context["techno_news_category"] = "Texno"

        return context

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Mahalliy")

        return news


class ForeignNewsListView(ListView):
    model = News
    template_name = "news/foreign-news-list.html"
    context_object_name = "foreign_news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foreign_news"] = News.published.all().filter(category__name="Xorijiy")
        context["techno_news"] = News.published.all().filter(category__name="Texno")
        context["sport_news"] = News.published.all().filter(category__name="Sport")
        context["categories"] = Category.objects.all()
        context["local_news_category"] = "Mahalliy"
        context["sport_news_category"] = "Sport"
        context["techno_news_category"] = "Texno"

        return context

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Xorijiy")

        return news


class TechnoNewsListView(ListView):
    model = News
    template_name = "news/techno-news-list.html"
    context_object_name = "techno_news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foreign_news"] = News.published.all().filter(category__name="Xorijiy")
        context["techno_news"] = News.published.all().filter(category__name="Texno")
        context["sport_news"] = News.published.all().filter(category__name="Sport")
        context["categories"] = Category.objects.all()
        context["local_news_category"] = "Mahalliy"
        context["sport_news_category"] = "Sport"
        context["techno_news_category"] = "Texno"

        return context

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Texno")

        return news


class SportNewsListView(ListView):
    model = News
    template_name = "news/sport-news-list.html"
    context_object_name = "sport_news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foreign_news"] = News.published.all().filter(category__name="Xorijiy")
        context["techno_news"] = News.published.all().filter(category__name="Texno")
        context["sport_news"] = News.published.all().filter(category__name="Sport")
        context["categories"] = Category.objects.all()
        context["local_news_category"] = "Mahalliy"
        context["sport_news_category"] = "Sport"
        context["techno_news_category"] = "Texno"

        return context

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Sport")

        return news
