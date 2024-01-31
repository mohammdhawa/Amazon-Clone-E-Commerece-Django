# Generated by Django 4.2 on 2024-01-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('SALE', 'SALE'), ('NEW', 'NEW'), ('FEATURE', 'FEATURE')], max_length=20, verbose_name='flag'),
        ),
    ]