# Generated by Django 4.0.6 on 2022-08-07 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='Summary',
            new_name='summary',
        ),
    ]
