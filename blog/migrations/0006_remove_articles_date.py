# Generated by Django 4.0.2 on 2022-03-29 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_articles_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='date',
        ),
    ]
