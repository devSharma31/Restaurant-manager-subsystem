# Generated by Django 4.2.1 on 2023-05-10 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_acc_ms', '0001_initial'),
        ('menu_ms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='Menus',
        ),
    ]
