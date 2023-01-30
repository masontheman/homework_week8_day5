# Generated by Django 4.1.5 on 2023-01-27 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=80)),
                ("thumb", models.ImageField(upload_to="thumbnails/")),
                ("video", models.FileField(upload_to="videos/")),
                ("views", models.IntegerField(default=0)),
                ("likes", models.IntegerField(default=0)),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
                ("desc", models.TextField(max_length=5000)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
