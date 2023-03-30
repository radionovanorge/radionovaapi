# Generated by Django 4.1.7 on 2023-03-16 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("radionova", "0004_alter_post_created_alter_post_updated"),
    ]

    operations = [
        migrations.CreateModel(
            name="Images",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="radionova.post",
                    ),
                ),
            ],
            options={
                "db_table": "images",
            },
        ),
    ]
