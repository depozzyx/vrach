# pylint: disable=signature-differs, no-member
from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "fullname", "city", "profession", "professions")
    list_filter = ("profession",)

    def professions(self, obj: models.User):
        professions_to_users = models.ProfessionToUser.objects.filter(
            user_id=obj.user_id
        )
        titles = [
            models.Profession.objects.get(profession_id=p.profession_id).title
            for p in professions_to_users
        ]
        return ", ".join(titles)


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
