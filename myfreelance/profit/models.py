from django.db import models


class Project(models.Model):
    name = models.CharField(verbose_name='Название проекта', blank=False, max_length=100)
    client = models.CharField(verbose_name='Заказчик', blank=False, max_length=100)
    platform = models.CharField(verbose_name='Платформа', blank=True, max_length=100)
    start_date = models.DateField(verbose_name='Дата начала', auto_now_add=True)

    server = models.CharField(verbose_name='Сервер', blank=True, max_length=100)
    server_info = models.TextField(verbose_name='Данные сервера', null=True, blank=True, max_length=10000)

    is_server_mine = models.BooleanField(verbose_name='На моём сервере', blank=True, null=True)
    rent_price = models.IntegerField(verbose_name='Стоимость аренды сервера', blank=True, null=True)
    rent_next_payment_date = models.DateField(verbose_name='Дата следующей оплаты сервера', blank=True, null=True)

    support = models.BooleanField(verbose_name='Поддержка', default=False, blank=True, null=True)
    support_price = models.IntegerField(verbose_name='Цена поддержки', blank=True, null=True)
    support_next_payment_date = models.DateField(verbose_name='Дата следующей оплаты поддержки', blank=True, null=True)

    project_price = models.IntegerField(verbose_name='Цена', blank=False)

    description = models.TextField(verbose_name='Описание', blank=True, max_length=10000)
    comment = models.TextField(verbose_name='Комментарий', blank=True, max_length=10000)

    income = models.IntegerField(verbose_name='Заплачено', blank=True)
    debt = models.IntegerField(verbose_name='Долг', null=True, blank=True)
    finish_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    status = models.BooleanField(verbose_name='Статус', default=False)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-start_date']

    def __str__(self):
        return str(self.name)


class AdditionalPayments(models.Model):
    project = models.ForeignKey(to='Project', blank=False, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', blank=True, max_length=10000)
    comment = models.TextField(verbose_name='Комментарий', blank=True, max_length=10000)
    price = models.IntegerField(verbose_name='Цена', blank=False)
    payment_date = models.DateField(verbose_name='Дата оплаты', auto_now_add=True)

    class Meta:
        verbose_name = 'Доп Приход'
        verbose_name_plural = 'Доп Приход'
        ordering = ['-payment_date']

    def __str__(self):
        return '+ Приход --- ', str(self.project)


class SupportPayments(models.Model):
    project = models.ForeignKey(to='Project', blank=False, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', blank=True, max_length=10000)
    comment = models.TextField(verbose_name='Комментарий', blank=True, max_length=10000)
    price = models.IntegerField(verbose_name='Цена', blank=False)
    payment_date = models.DateField(verbose_name='Дата оплаты', auto_now_add=True)

    class Meta:
        verbose_name = 'Поддержка Приход'
        verbose_name_plural = 'Поддержка Приход'
        ordering = ['-payment_date']

    def __str__(self):
        return '+ Поддержка Приход --- ', str(self.project)


class Portfolio(models.Model):
    PROJECT_TYPE = [('web', 'web'),
                    ('bot', 'bot'),
                    ('desktop', 'desktop')]
    project_type = models.CharField(max_length=300, choices=PROJECT_TYPE, blank=False, null=False,
                                    verbose_name='Тип Проекта')
    name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Название проекта  ')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    description = models.TextField(null=False, blank=False, max_length=10000, verbose_name='Описание')
    date = models.DateField(null=False, blank=False, verbose_name='Дата начала работ')
    url = models.URLField(null=True, blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект портфолио'
        verbose_name_plural = 'Проекты портфолио'
