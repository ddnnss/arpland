from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices

import string


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    first_name = None
    last_name = None
    order_number = models.IntegerField('Порядок отображения', default=0)
    email = models.EmailField('Эл. почта', unique=True)
    name = models.CharField('ФИО', max_length=50, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True)
    avatar = models.ImageField('Фото профиля', upload_to='avatar/', blank=True)
    organization_name = models.CharField('Название организации', max_length=100, blank=False, null=True)
    organization_name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False)
    organization_site = models.CharField('Сайт организации (без http)', max_length=50, blank=True, null=True)
    organization_address = models.TextField('Адрес организации', blank=True, null=True)
    organization_description = RichTextUploadingField('Полное описание организации', blank=True, null=True)
    organization_short_description = models.CharField('Краткое описание организации', max_length=100, blank=True, null=True)
    organization_avatar = models.ImageField('Фото организации', upload_to='avatar/', blank=True)
    organization_vk = models.CharField('Ссылка на VK', max_length=100, blank=True, null=True)
    organization_fb = models.CharField('Ссылка на FB', max_length=100, blank=True, null=True)
    organization_inst = models.CharField('Ссылка на Instagram', max_length=100, blank=True, null=True)
    organization_yt = models.CharField('Ссылка на YouTube', max_length=100, blank=True, null=True)
    organization_ok = models.CharField('Ссылка на OK', max_length=100, blank=True, null=True)
    organization_views = models.IntegerField('Просмотров', default=0)
    profile_ok = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    @property
    def get_avatar(self):
        if self.organization_avatar:
            return self.organization_avatar.url
        else:
            return 'data:image/png;base64,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'

    def save(self, *args, **kwargs):
        slug = slugify(self.organization_name)
        testSlug = User.objects.filter(organization_name_slug=slug)
        slugRandom = ''
        if not self.organization_name_slug:
            slug = slugify(self.organization_name)
            testSlug = User.objects.filter(organization_name_slug=slug)
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
                self.organization_name_slug = slug + slugRandom
            else:
                self.organization_name_slug = slug

        super(User, self).save(*args, **kwargs)

    @property
    def get_company_avatar(self):
        if self.organization_avatar and hasattr(self.organization_avatar, 'url'):
            return self.organization_avatar.url
        else:
            return "http://placehold.it/900x500"




