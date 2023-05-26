from django.urls import reverse
from django.utils import timezone
from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)


class ActivedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Staff.Status.Active)


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model):
    """
    News class
    If we delete any category, the connected news will also be deleted.
    """

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to="news/images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Draft
    )

    objects = models.Manager()  # defauld manager
    published = PublishedManager()

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_page", args=[self.slug])


class Occupation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Staff(models.Model):
    class Status(models.TextChoices):
        Active = "AT", "Active"
        Disable = "DS", "Disable"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_info = models.TextField()
    image = models.ImageField(upload_to="staff/images")
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Active
    )

    objects = models.Manager()  # defauld manager
    active = ActivedManager()

    # class Meta:
    #     ordering = ["-published_time"]

    def __str__(self):
        return self.first_name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email
