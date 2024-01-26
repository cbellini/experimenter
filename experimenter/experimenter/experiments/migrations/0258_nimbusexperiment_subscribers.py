# Generated by Django 3.2.23 on 2024-01-22 20:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("experiments", "0257_alter_nimbusexperiment_qa_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="subscribers",
            field=models.ManyToManyField(
                blank=True,
                related_name="subscribed_nimbusexperiments",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Subscribers",
            ),
        ),
    ]