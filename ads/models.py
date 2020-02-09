from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
from customuser.views import User
import string

class AdTextPost(models.Model):
    name = models.CharField('Название ', max_length=200, blank=False, null=True)
    author = models.ForeignKey(User, blank=True, null=True, verbose_name='Автор', on_delete=models.CASCADE)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False)
    image = models.ImageField('Изображение превью ', upload_to='ad_text_img/', blank=False)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=True, null=True, editable=False)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True, editable=False)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True, editable=False)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True, editable=False)
    short_description = models.CharField('Краткое описание ', max_length=200, blank=True)
    description = RichTextUploadingField('Текст объявления', blank=True, null=True)
    views = models.IntegerField('Просмотров', default=0)
    is_active = models.BooleanField('Отображать статью ?', default=True, db_index=True)
    is_published = models.BooleanField('Опубликовано?', default=True)
    is_published_at_index = models.BooleanField('Показывать на главной', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        slugRandom = ''
        if not self.name_slug:
            testSlug = AdTextPost.objects.filter(name_slug=slug)
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
                self.name_slug = slug + slugRandom
            else:
                self.name_slug = slug
        self.name_lower = self.name.lower()
        super(AdTextPost, self).save(*args, **kwargs)
    # def get_absolute_url(self):
    #     return f'/post/{self.name_slug}/'

    def __str__(self):
        return 'Текстовое обьявление : %s ' % self.name

    class Meta:
        verbose_name = "Текстовое обьявление"
        verbose_name_plural = "Текстовые обьявления"

class AdVideoPost(models.Model):
    name = models.CharField('Название ', max_length=200, blank=False, null=True)
    author = models.ForeignKey(User, blank=True, null=True, verbose_name='Автор', on_delete=models.SET_NULL)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False)
    image = models.ImageField('Изображение превью ', upload_to='ad_video_img/', blank=False)
    video_link = models.CharField('Видео ID', max_length=100, blank=False, null=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=True, null=True, editable=False)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True, editable=False)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True, editable=False)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True, editable=False)
    short_description = models.CharField('Краткое описание ', max_length=200, blank=True)
    description = RichTextUploadingField('Текст объявления', blank=True, null=True)
    views = models.IntegerField('Просмотров', default=0)
    is_published = models.BooleanField('Опубликовано?', default=True)
    is_active = models.BooleanField('Отображать  ?', default=True, db_index=True)
    is_published_at_index = models.BooleanField('Показывать на главной', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        slugRandom = ''
        if not self.name_slug:
            testSlug = AdVideoPost.objects.filter(name_slug=slug)
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
                self.name_slug = slug + slugRandom
            else:
                self.name_slug = slug
        self.name_lower = self.name.lower()
        super(AdVideoPost, self).save(*args, **kwargs)
    # def get_absolute_url(self):
    #     return f'/post/{self.name_slug}/'

    def __str__(self):
        return 'Видео обьявление : %s ' % self.name

    class Meta:
        verbose_name = "Видео обьявление"
        verbose_name_plural = "Видео обьявления"