# Generated by Django 2.2.1 on 2019-06-07 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Team', '0008_auto_20190606_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='user_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
