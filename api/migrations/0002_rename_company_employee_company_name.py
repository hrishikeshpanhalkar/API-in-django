# Generated by Django 4.1.5 on 2023-01-27 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='company',
            new_name='company_name',
        ),
    ]
