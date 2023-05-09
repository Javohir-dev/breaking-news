from django.urls import path
from .views import news_list, detail_page


urlpatterns = [
    path("all/", news_list, name="news_list_page"),
    path("<int:id>/", detail_page, name="detail_page"),
]
