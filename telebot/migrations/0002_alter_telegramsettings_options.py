# Generated by Django 4.0.1 on 2022-05-25 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telebot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegramsettings',
            options={'verbose_name': 'Настройки бота', 'verbose_name_plural': 'Настройки бота'},
        ),
    ]
