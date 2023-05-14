from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()
    context = {"news_list": news_list}

    return render(request, "news/news_list.html", context)


def detail_page(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {"news": news}

    return render(request, "news/detail.html", context)


def homePageView(request):
    news = News.published.all()
    category = Category.objects.all()
    context = {"news": news, "category": category}

    return render(request, "news/home.html", context)


def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        # return HttpResponse("<h1>Thank you for message!</h1>")

    context = {"form": form}

    return render(request, "news/contact.html", context)


def errorPageView(request):
    context = {}

    return render(request, "news/404-page.html", context)
