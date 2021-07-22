# Generated by Django 3.2.5 on 2021-07-22 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0004_staffarchive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(help_text='Тема сообщения', max_length=150)),
                ('content', models.TextField(help_text='Текст сообщения')),
                ('send_datetime', models.DateTimeField(help_text='Дата сообщения')),
                ('closed', models.BooleanField()),
                ('addressee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks2', to='staff.staff')),
                ('sender_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='staff.staff')),
            ],
        ),
    ]