# Generated by Django 5.0.7 on 2024-08-03 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_created_todo_create_alter_todo_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='create',
            new_name='created',
        ),
    ]
