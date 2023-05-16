from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()
    context = {"news_list": news_list}

    return render(request, "news/news_list.html", context)


def detail_page(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {"news": news}

    return render(request, "news/single-post.html", context)


def homePageView(request):
    news_list = News.published.all().order_by("-published_time")[:5]
    category = Category.objects.all()
    context = {"news_list": news_list, "category": category}

    return render(request, "news/home.html", context)


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
