# Generated by Django 3.2.12 on 2022-09-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='img_url',
            field=models.TextField(null=True, verbose_name='썸네일 이미지'),
        ),
    ]
