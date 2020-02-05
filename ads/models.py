from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
from customuser.views import User
import string

class AdTextPost(models.Model):
    name = models.CharField('Название ', max_length=200, blank=False, null=True)
    author = models.ForeignKey(User, blank=True, null=True, verbose_name='Автор', on_delete=models.SET_NULL)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение превью ', upload_to='ad_text_img/', blank=False)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)
    short_description = models.CharField('Краткое описание ', max_length=200, blank=True)
    description = RichTextUploadingField('Текст объявления', blank=True, null=True)
    views = models.IntegerField('Просмотров', default=0)
    is_active = models.BooleanField('Отображать статью ?', default=True, db_index=True)
    is_published = models.BooleanField('Опубликовано?', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        testSlug = AdTextPost.objects.filter(name_slug=slug)
        slugRandom = ''
        if not testSlug:
            slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
        self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(AdTextPost, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return f'/post/{self.name_slug}/'

    def __str__(self):
        return 'Текстовое обьявление : %s ' % self.name

    class Meta:
        verbose_name = "Текстовое обьявление"
        verbose_name_plural = "Текстовые обьявления"

class AdVideoPost(models.Model):
    name = models.CharField('Название ', max_length=200, blank=False, null=True)
    author = models.ForeignKey(User, blank=True, null=True, verbose_name='Автор', on_delete=models.SET_NULL)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение превью ', upload_to='ad_video_img/', blank=False)
    video_link = models.CharField('Ссылка на YouTube ', max_length=100, blank=False, null=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)
    short_description = models.CharField('Краткое описание ', max_length=200, blank=True)
    description = RichTextUploadingField('Текст объявления', blank=True, null=True)
    views = models.IntegerField('Просмотров', default=0)
    is_published = models.BooleanField('Опубликовано?', default=True)
    is_active = models.BooleanField('Отображать статью ?', default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        testSlug = AdVideoPost.objects.filter(name_slug=slug)
        slugRandom = ''
        if not testSlug:
            slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
        self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(AdVideoPost, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return f'/post/{self.name_slug}/'

    def __str__(self):
        return 'Текстовое обьявление : %s ' % self.name

    class Meta:
        verbose_name = "Текстовое обьявление"
        verbose_name_plural = "Текстовые обьявления"