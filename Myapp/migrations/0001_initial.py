# Generated by Django 3.2.17 on 2023-03-18 23:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(120)])),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
