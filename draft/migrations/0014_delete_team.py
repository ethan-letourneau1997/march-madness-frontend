# Generated by Django 4.1.7 on 2023-03-12 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0013_group_last_person_picking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Team',
        ),
    ]