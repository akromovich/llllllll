# Generated by Django 4.0.2 on 2022-03-04 05:33

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_work_tel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=10000, verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=10000, null=True, verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=10000, null=True, verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=10000, null=True, verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=10000, verbose_name='Название статьи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=10000, null=True, verbose_name='Название статьи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=10000, null=True, verbose_name='Название статьи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_uz',
            field=models.CharField(max_length=10000, null=True, verbose_name='Название статьи'),
        ),
    ]
