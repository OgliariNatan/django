# Generated by Django 4.2.4 on 2024-12-23 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="choice",
            old_name="Choice_text",
            new_name="choice_text",
        ),
    ]