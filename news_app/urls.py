from django.urls import path
from .views import news_list, detail_page, homePageView


urlpatterns = [
    path("", homePageView, name="home_page"),
    path("news/", news_list, name="news_list_page"),
    path("news/<int:id>/", detail_page, name="detail_page"),
]
