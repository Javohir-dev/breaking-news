from django.shortcuts import render, get_object_or_404
from .models import News, Category


def news_list(request):
    news_list = News.published.all()
    context = {"news_list": news_list}

    return render(request, "news/news_list.html", context)


def detail_page(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {"news": news}

    return render(request, "news/detail.html", context)
