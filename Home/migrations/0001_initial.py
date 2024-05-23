# Generated by Django 5.0.6 on 2024-05-23 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cetagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_cetagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Sub Cetagory')),
                ('cetagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.cetagory', verbose_name='Main Cetagory')),
            ],
            options={
                'verbose_name': 'Sub Cetagory',
            },
        ),
    ]