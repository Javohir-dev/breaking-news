from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import user_login


urlpatterns = [
    # path("login/", user_login, name="login_page"),
    path("login/", LoginView.as_view(), name="login_page"),
    path("logout/", LogoutView.as_view(), name="logout_page"),
]
