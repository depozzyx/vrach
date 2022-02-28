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
    list_display = ("profession_id", "title")


@admin.register(models.ProfessionToUser)
class ProfessionToUserAdmin(admin.ModelAdmin):
    list_display = ("user", "profession")


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "user")


@admin.register(models.ProfessionToQuestion)
class ProfessionToQuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "profession")
