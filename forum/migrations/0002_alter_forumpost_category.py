# Generated by Django 5.2.2 on 2025-06-05 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="forumpost",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="forum.forumcategory",
            ),
        ),
    ]
