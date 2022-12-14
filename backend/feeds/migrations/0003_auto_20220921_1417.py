# Generated by Django 3.2.12 on 2022-09-21 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0002_alter_feed_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedcomment',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed_comments', to='feeds.feed', verbose_name='남의 정원 PK'),
        ),
        migrations.AlterField(
            model_name='feedcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed_comments', to=settings.AUTH_USER_MODEL, verbose_name='내 아이디'),
        ),
    ]
