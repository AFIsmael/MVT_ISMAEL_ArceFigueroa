# Generated by Django 4.1.2 on 2022-10-18 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='age',
            new_name='date_birth',
        ),
    ]
