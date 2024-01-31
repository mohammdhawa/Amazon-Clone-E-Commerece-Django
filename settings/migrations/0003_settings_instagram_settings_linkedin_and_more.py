# Generated by Django 4.2 on 2024-01-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_settings_address_alter_settings_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='pinterest',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]