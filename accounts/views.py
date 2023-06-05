from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, View
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


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
    profile = Profile.objects.get(user=user)

    context = {
        "user": user,
        "profile": profile,
    }

    return render(request, "registration/profile.html", context)


def user_reginter(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {"new_user": new_user}
            return render(request, "account/register-done.html", context)

    else:
        form = UserRegistrationForm()
        context = {"form": form}

        return render(request, "account/register.html", {"form": form})


# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login_page")
#     template_name = "account/register.html"


class SignUpView(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {"form": form}

        return render(request, "account/register.html", context)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            context = {"new_user": new_user}
            return render(request, "account/register-done.html", context)


def user_edit(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "profile": profile,
    }
    return render(request, "account/profile-edit.html", context)
