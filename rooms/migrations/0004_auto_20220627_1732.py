# Generated by Django 2.2.5 on 2022-06-27 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20220627_1730'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Amenities',
            new_name='Amenity',
        ),
    ]
