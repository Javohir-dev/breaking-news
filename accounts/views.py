from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, TemplateView
from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data["username"],
                password=data["password"],
            )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Successfully registered!")
            else:
                return HttpResponse("Failed to register successfully!")
        else:
            return HttpResponse("There is an error in username or password!")
    else:
        form = LoginForm()

    context = {"form": form}
    return render(request, "registration/login.html", context)


class UserProfileView(TemplateView):
    template_name = "registration/profile.html"


def dashboard_view(request):
    user = request.user

    context = {"user": user}

    return render(request, "registration/profile.html")
