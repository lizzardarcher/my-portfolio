from django.db import models


class TgChannel(models.Model):
    title = models.CharField(max_length=300, unique=True, null=False, blank=False, verbose_name="Название")
    link = models.CharField(max_length=300, unique=True, null=False, blank=False, verbose_name="Ссылка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Телеграм Канал"
        verbose_name_plural = "Телеграм Каналы"


class TgChat(models.Model):
    title = models.CharField(max_length=300, unique=True, null=False, blank=False, verbose_name="Название")
    link = models.CharField(max_length=300, unique=True, null=False, blank=False, verbose_name="Ссылка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Телеграм Группа"
        verbose_name_plural = "Телеграм Группы"


class Settings(models.Model):
    auto_reply_message = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Сообщение для автоответчика")
    common_message = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Сообщение для рассылки")
    auto_reply_delay = models.IntegerField(default=0, null=False, blank=False, verbose_name="Задержка для автоответчика")
    common_message_delay = models.IntegerField(default=0, null=False, blank=False, verbose_name="Задержка между сообщениями")
    api_id = models.IntegerField(default=0, null=False, blank=False, verbose_name="api id")
    api_hash = models.CharField(max_length=150, null=False, blank=False, verbose_name="api hash")
    phone = models.CharField(max_length=15, null=False, blank=False, verbose_name="Phone")
    username = models.CharField(max_length=150, null=False, blank=False, verbose_name="Username")
    session = models.FileField(max_length=1500, null=True, blank=True, verbose_name="Session File")

    def __str__(self):
        return 'Настройки проекта по поиску фриланс заказов'

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"


class AllowedWord1Level(models.Model):
    word = models.CharField(max_length=30, null=False, blank=False, verbose_name="Слово")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "#1 Ключевое слово 1 уровня"
        verbose_name_plural = "#1 Ключевые слова 1 уровня"


class AllowedWord2Level(models.Model):
    word = models.CharField(max_length=30, null=False, blank=False, verbose_name="Слово")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "#2 Ключевое слово 2 уровня"
        verbose_name_plural = "#2 Ключевые слова 2 уровня"


class DisallowedWord(models.Model):
    word = models.CharField(max_length=30, null=False, blank=False, verbose_name="Слово")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "#3 Запрещенное слово"
        verbose_name_plural = "#3 Запрещенные слова"


class ExcludeWord(models.Model):
    word = models.CharField(max_length=30, null=False, blank=False, verbose_name="Слово")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "#4 Слово для исключения"
        verbose_name_plural = "#4 Слова для исключения"

