from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from .views import dashboard_view, user_reginter, SignUpView, EditUserView, user_edit


urlpatterns = [
    # path("login/", user_login, name="login_page"),
    path("signup/", SignUpView.as_view(), name="register_page"),
    path("login/", LoginView.as_view(), name="login_page"),
    path("logout/", LogoutView.as_view(), name="logout_page"),
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path(
        "password-change-done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("profile/", dashboard_view, name="profile_page"),
    path("edit-profile/", EditUserView.as_view(), name="edit_profile_page"),
    # path("edit-profile/", user_edit, name="edit_profile_page"),
]
