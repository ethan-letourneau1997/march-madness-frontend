# Generated by Django 4.1.7 on 2023-03-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0010_alter_people_options_alter_player_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='draft_active',
            field=models.BooleanField(default=True),
        ),
    ]