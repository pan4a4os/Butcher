from django.db import models


class Articles(models.Model):
    name = models.CharField('Ім’я', max_length=25)
    phone_number = models.CharField('Номер телефону',max_length=12)
    notice = models.TextField('Повідомлення')
    data = models.DateTimeField('yyyy-mm-dd hh:mm')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = "Повідомлення"