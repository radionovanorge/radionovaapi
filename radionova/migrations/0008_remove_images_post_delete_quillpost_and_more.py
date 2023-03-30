# Generated by Django 4.1.7 on 2023-03-30 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("radionova", "0007_quillpost"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="images",
            name="post",
        ),
        migrations.DeleteModel(
            name="QuillPost",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="body",
            new_name="content",
        ),
        migrations.RemoveField(
            model_name="post",
            name="heading",
        ),
        migrations.DeleteModel(
            name="Images",
        ),
    ]