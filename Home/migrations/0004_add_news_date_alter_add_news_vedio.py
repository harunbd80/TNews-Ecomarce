# Generated by Django 5.0.6 on 2024-05-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_add_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_news',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='add_news',
            name='vedio',
            field=models.FileField(blank=True, null=True, upload_to='Vedeos/'),
        ),
    ]
