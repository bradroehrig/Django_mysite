# Generated by Django 4.1 on 2022-10-31 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updatd',
            new_name='updated',
        ),
    ]
