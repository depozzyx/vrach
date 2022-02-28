# pylint: disable=signature-differs, no-member
from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "fullname", "city", "profession")


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("city_id", "title")


@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("profession_id", "profession_type", "title")


@admin.register(models.ProfessionToUser)
class ProfessionToUserAdmin(admin.ModelAdmin):
    list_display = ("user", "profession")
