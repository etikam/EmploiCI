# Generated by Django 5.1.1 on 2024-09-21 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmploiApp', '0005_seance_profdispoweek_alter_group_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seance',
            old_name='ProfDispoWeek',
            new_name='profDispoWeek',
        ),
    ]
