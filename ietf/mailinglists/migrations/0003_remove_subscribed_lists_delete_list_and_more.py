# Generated by Django 4.2.9 on 2024-02-02 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailinglists", "0002_nonwgmailinglist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscribed",
            name="lists",
        ),
        migrations.DeleteModel(
            name="List",
        ),
        migrations.DeleteModel(
            name="Subscribed",
        ),
    ]