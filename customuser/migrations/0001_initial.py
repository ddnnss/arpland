# Generated by Django 2.1.5 on 2020-02-23 07:32

import ckeditor_uploader.fields
import customuser.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('order_number', models.IntegerField(default=0, verbose_name='Порядок отображения')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Эл. почта')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/', verbose_name='Фото профиля')),
                ('profile_ok', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', customuser.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название организации')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('site', models.CharField(blank=True, max_length=50, null=True, verbose_name='Сайт организации (без http)')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес организации')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Полное описание организации')),
                ('short_description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Краткое описание организации')),
                ('avatar', models.ImageField(blank=True, upload_to='company/', verbose_name='Фото организации')),
                ('vk', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на VK')),
                ('fb', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на FB')),
                ('inst', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на Instagram')),
                ('yt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на YouTube')),
                ('ok', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на OK')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Принадлежит пользователю')),
            ],
        ),
    ]
