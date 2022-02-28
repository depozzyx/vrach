# Generated by Django 3.1.2 on 2022-02-28 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20220228_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profession',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(choices=[('med', 'Медик'), ('pacient', 'Пациент')], default='med', max_length=128, verbose_name='Тип проффесии'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProfessionToUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.profession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.user')),
            ],
        ),
    ]
