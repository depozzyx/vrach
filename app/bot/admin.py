# pylint: disable=signature-differs, no-member
from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin:
    pass


@admin.register(models.City)
class CityAdmin:
    pass


@admin.register(models.Profession)
class ProfessionAdmin:
    pass
