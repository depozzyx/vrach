# Generated by Django 3.1.2 on 2022-02-28 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20220228_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closed', models.BooleanField(verbose_name='Закрыт?')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.user')),
            ],
            options={
                'db_table': 'admin_panel_question',
            },
        ),
    ]
