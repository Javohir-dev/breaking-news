from django.urls import path
from .views import news_list, detail_page, homePageView, contactPageView, errorPageView


urlpatterns = [
    path("", homePageView, name="home_page"),
    path("news/", news_list, name="news_list_page"),
    path("news/<int:id>/", detail_page, name="detail_page"),
    path("contact/", contactPageView, name="contact_page"),
    path("404/", errorPageView, name="404_page"),
]
