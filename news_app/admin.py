from django.contrib import admin
from .models import News, Category, Contact, Staff, Occupation


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "published_time", "status", "category"]
    list_filter = ["status", "created_time", "published_time", "category"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_time"
    search_fields = ["title", "body"]
    ordering = ["status", "published_time"]


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "occupation", "status"]


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


# admin.site.register(News)
# admin.site.register(Category)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message"]
