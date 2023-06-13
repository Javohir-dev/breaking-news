from django import forms
from .models import Contact, News, Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        # fields = "__all__"


class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "body", "image", "category", "status"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.TextInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user", "body"]
