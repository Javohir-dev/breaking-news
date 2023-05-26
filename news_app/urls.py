from django.urls import path
from .views import (
    news_list,
    detail_page,
    HomePageView,
    ContactPageView,
    ErrorPageView,
    LocalNewsListView,
    ForeignNewsListView,
    TechnoNewsListView,
    SportNewsListView,
    AboutView,
    StaffPageView,
)


urlpatterns = [
    # path("", homePageView, name="home_page"),
    path("", HomePageView.as_view(), name="home_page"),
    path("news/", news_list, name="news_list_page"),
    path("news/<slug:news>/", detail_page, name="detail_page"),
    path("contact/", ContactPageView.as_view(), name="contact_page"),
    path("404/", ErrorPageView.as_view(), name="404_page"),
    path("local/", LocalNewsListView.as_view(), name="local_news_page"),
    path("foreign/", ForeignNewsListView.as_view(), name="foreign_news_page"),
    path("texno/", TechnoNewsListView.as_view(), name="texno_news_page"),
    path("sport/", SportNewsListView.as_view(), name="sport_news_page"),
    path("about-us/", AboutView.as_view(), name="about_page"),
    path("staff/", StaffPageView.as_view(), name="staff_page"),
]
