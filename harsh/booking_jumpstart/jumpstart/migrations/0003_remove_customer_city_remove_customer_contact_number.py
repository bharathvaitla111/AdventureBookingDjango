# Generated by Django 4.1.7 on 2023-02-23 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jumpstart', '0002_alter_customer_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='contact_number',
        ),
    ]