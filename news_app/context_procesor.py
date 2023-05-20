from .models import News, Category


def top_news(request):
    categories = Category.objects.all()
    top_news = News.published.all().order_by("-published_time")[:4]

    context = {
        "top_news": top_news,
        "categories": categories,
    }

    return context
