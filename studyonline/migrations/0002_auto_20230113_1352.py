# Generated by Django 2.2 on 2023-01-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyonline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]
