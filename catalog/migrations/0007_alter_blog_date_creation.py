# Generated by Django 5.0.7 on 2024-07-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0006_alter_blog_date_creation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date_creation",
            field=models.DateField(blank=True, null=True, verbose_name="Дата создания"),
        ),
    ]
