# Generated by Django 4.1.7 on 2023-03-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("radionova", "0002_post_author_post_program"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=models.TextField(default=" "),
            preserve_default=False,
        ),
    ]