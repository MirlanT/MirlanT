# Generated by Django 4.0.5 on 2022-06-22 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]