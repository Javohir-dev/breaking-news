from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, TemplateView
from .forms import LoginForm, UserRegistrationForm


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

    return render(request, "registration/profile.html", context)


def user_reginter(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            context = {"new_user": new_user}
            return render(request, "account/register-done.html", context)

    else:
        form = UserRegistrationForm()
        context = {"form": form}

        return render(request, "account/register.html", {"form": form})
