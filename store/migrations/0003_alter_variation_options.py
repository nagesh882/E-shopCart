# Generated by Django 5.0.4 on 2024-06-11 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variation',
            options={'verbose_name': 'Variation', 'verbose_name_plural': 'Variations'},
        ),
    ]