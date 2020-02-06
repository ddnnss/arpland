from django.db import models

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
