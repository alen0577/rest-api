# Generated by Django 3.2.13 on 2022-06-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='images/None/noimg.jpg', upload_to='images/'),
        ),
    ]
