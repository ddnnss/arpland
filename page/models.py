from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
from customuser.views import User
import string

class Banner(models.Model):
    order = models.IntegerField('Порядок отображения', default=1)

    image = models.ImageField('Картинка', upload_to='banners/', blank=False, null=True)
    big_text = models.CharField('Большой текст', max_length=255, blank=False, null=True)
    small_text = models.TextField('Маленький текст', blank=False, null=True)
    url_text1 = models.CharField('Надпись на кнопке 1', max_length=255, blank=True, null=True)
    url_text2 = models.CharField('Надпись на кнопке 2', max_length=255, blank=True, null=True)
    url_link1 = models.CharField('Ссылка на кнопке 1', max_length=255, blank=True, null=True)
    url_link2 = models.CharField('Ссылка на кнопке 2', max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Баннер, порядковый номер : %s' % self.order

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"


class BlackList(models.Model):
    WORKER = 'W'
    CUSTOMER = 'C'

    BLACKLISTTYPE = [
        (WORKER, 'Исполнитель'),
        (CUSTOMER, 'Заказчик'),

    ]
    blackListType = models.CharField('Тип',
        max_length=2,
        choices=BLACKLISTTYPE,
        default=WORKER,
    )
    image = models.ImageField('Картинка', upload_to='banners/', blank=False, null=True)
    author = models.ForeignKey(User, blank=True, null=True, verbose_name='Автор', on_delete=models.CASCADE)
    name = models.CharField('Логин, ник, фио', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False)
    contacts = RichTextUploadingField('Все возможные контакты', blank=False, null=True)
    why = models.TextField('Причина добаления в список', blank=False, null=True)
    moneyLost = models.IntegerField('Материальный ущерб', blank=False, null=True)
    profile = models.CharField('Ссылка на профиль(отзыв о) исполнителя/заказчика на сайте, где возник инциден', max_length=255, blank=False, null=True)
    file = models.FileField('Загрузка переписки', upload_to='blacklist/')
    isAgreed = models.BooleanField('Устанавливая флажок я выражаю свое согласие на обработку персональных данных', default=False)
    isModerated = models.BooleanField('Подтверждено?',
                                   default=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        slugRandom = ''
        if not self.name_slug:
            testSlug = BlackList.objects.filter(name_slug=slug)
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
                self.name_slug = slug + slugRandom
            else:
                self.name_slug = slug

        super(BlackList, self).save(*args, **kwargs)

    def __str__(self):
        return f'Заявка в черный список'

    class Meta:
        verbose_name = "Заявка в черный список"
        verbose_name_plural = "Заявки в черный список"

class Contact(models.Model):
    address = RichTextUploadingField('Адрес', blank=True, null=True)
    phone = RichTextUploadingField('Телефон', blank=True, null=True)
    email = RichTextUploadingField('EMail', blank=True, null=True)
    about_info = RichTextUploadingField('Текст на страницу О нас', blank=True, null=True)
    slider1_text = models.CharField('Слайдер1 текст', max_length=255, blank=False, null=True)
    slider1_num = models.IntegerField('Слайдер1 Значание', blank=False, null=True, default=0)
    slider2_text = models.CharField('Слайдер2 текст', max_length=255, blank=False, null=True)
    slider2_num = models.IntegerField('Слайдер2 Значание', blank=False, null=True, default=0)
    slider3_text = models.CharField('Слайдер3 текст', max_length=255, blank=False, null=True)
    slider3_num = models.IntegerField('Слайдер3 Значание', blank=False, null=True, default=0)
    slider4_text = models.CharField('Слайдер4 текст', max_length=255, blank=False, null=True)
    slider4_num = models.IntegerField('Слайдер4 Значание', blank=False, null=True, default=0)



    def __str__(self):
        return 'Контакты и О нас'

    class Meta:
        verbose_name = "Контакты и О нас"
        verbose_name_plural = "Контакты и О нас"