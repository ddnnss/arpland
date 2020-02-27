# Generated by Django 2.1.5 on 2020-02-27 15:22

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='investor/', verbose_name='Фото')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('short_description', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Короткое описание')),
                ('full_description', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Полное описание')),
            ],
            options={
                'verbose_name': 'Инвестор',
                'verbose_name_plural': 'Инвесторы',
            },
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='tender/', verbose_name='Картинка')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('short_description', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Короткое описание')),
                ('full_description', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Полное описание')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Тендер',
                'verbose_name_plural': 'Тендеры',
            },
        ),
    ]