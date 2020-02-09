from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from customuser.views import User

class Banner(models.Model):
    order = models.IntegerField('Порядок отображения', default=1)

    image = models.ImageField('Картинка', upload_to='banners/', blank=False, null=True)
    big_text = models.CharField('Большой текст', max_length=255, blank=False, null=True)
    small_text = models.CharField('Маленький текст', max_length=255, blank=False, null=True)
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
    author = models.ForeignKey(User, blank=True, null=True, verbose_name='Автор', on_delete=models.CASCADE)
    name = models.CharField('Логин, ник, фио', max_length=255, blank=False, null=True)
    contacts = RichTextUploadingField('Все возможные контакты', blank=False, null=True)
    why = models.TextField('Причина добаления в список', blank=False, null=True)
    moneyLost = models.IntegerField('Материальный ущерб', blank=False, null=True)
    profile = models.CharField('Ссылка на профиль(отзыв о) исполнителя/заказчика на сайте, где возник инциден', max_length=255, blank=False, null=True)
    file = models.FileField('Загрузка переписки', upload_to='blacklist/')
    isAgreed = models.BooleanField('Устанавливая флажок я выражаю свое согласие на обработку персональных данных', default=False)
    isModerated = models.BooleanField('Подтверждено?',
                                   default=False)

    def __str__(self):
        return f'Заявка в черный список'

    class Meta:
        verbose_name = "Заявка в черный список"
        verbose_name_plural = "Заявки в черный список"