from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = ("username", "email", "language", "gender", "currency", "superhost")
    list_filter = ("superhost", "language", "currency")
