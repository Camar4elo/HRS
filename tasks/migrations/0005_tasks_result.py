# Generated by Django 3.2.5 on 2021-07-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20210722_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='result',
            field=models.TextField(help_text='Результат', null=True),
        ),
    ]