# Generated by Django 4.0.5 on 2022-06-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_article_status_alter_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, max_length=30, null=True, verbose_name='Дата'),
        ),
    ]