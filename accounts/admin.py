from django.contrib import admin
from .models import Profile


# admin.site.register(Profile)


# @admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "birth_date", "photo"]


admin.site.register(Profile, ProfileAdmin)
