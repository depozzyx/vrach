from django.db import models


class Profession(models.Model):
    PROFESSIONS = (("med", "Медик"), ("pacient", "Пациент"))

    profession_id = models.AutoField("ID", primary_key=True)
    title = models.CharField("Название", max_length=256)
    profession_type = models.CharField(
        "Тип проффесии", max_length=128, choices=PROFESSIONS
    )

    class Meta:
        db_table = "admin_panel_profession"

    def __str__(self):
        return f"Проффесия({self.profession_id} {self.title})"


class City(models.Model):
    city_id = models.AutoField("ID", primary_key=True)
    title = models.CharField("Город", max_length=256)

    class Meta:
        db_table = "admin_panel_city"

    def __str__(self):
        return f"Город({self.city_id} {self.title})"


class User(models.Model):
    user_id = models.IntegerField("User ID", primary_key=True)
    username = models.CharField("Юзернейм", null=True, blank=True, max_length=256)
    fullname = models.CharField("Имя", max_length=512)
    profession = models.CharField(
        "Тип проффесии", max_length=128, choices=Profession.PROFESSIONS, null=True
    )
    city = models.ForeignKey(
        City, verbose_name="Город", on_delete=models.CASCADE, null=True
    )
    create_date = models.DateTimeField("Создан", auto_now_add=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "admin_panel_botuser"

    def __str__(self):
        return f"Пользователь({self.user_id} {self.fullname})"


class ProfessionToUser(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "admin_panel_profession_to_user"


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    closed = models.BooleanField("Закрыт?")
    create_date = models.DateTimeField("Дата создания", auto_now_add=True)
    question = models.TextField("Вопрос")
    profession = models.ForeignKey(
        Profession,
        on_delete=models.SET_NULL,
        verbose_name="Направление вопроса",
        null=True,
    )

    class Meta:
        db_table = "admin_panel_question"
