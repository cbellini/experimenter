# Generated by Django 3.1.8 on 2021-05-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0167_auto_20210430_2031"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="risk_brand",
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="nimbusexperiment",
            name="risk_partner_related",
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="nimbusexperiment",
            name="risk_revenue",
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
