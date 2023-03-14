# Generated by Django 4.1.7 on 2023-03-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0002_team_logo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='team',
            name='team_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
