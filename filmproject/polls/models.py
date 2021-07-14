from django.db import models
import datetime
# Импортируем настройки приложения polls
from polls import settings


# Create your models here.
class Question(models.Model):
    """Вопрос"""
    title = models.CharField(max_length=200, verbose_name="Вопрос")
    date_published = models.DateTimeField(verbose_name="Дата публикации",
                                          default=datetime.datetime.now())
    is_active = models.BooleanField(verbose_name="Опубликован")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    # Этот метод позволяет выявить Популярный опрос для показа в админке
    def is_popular(self):
        answers = Answer.objects.filter(question_id=self.id)
        votes_total = sum([answer.votes for answer in answers])
        return votes_total > settings.POLLS_POPULAR_VOTES_LIMIT

    # Описание столбца в админке
    is_popular.short_description = 'Популярный'
    # Вот настройка, заменяющая False/True на иконки в админке
    is_popular.boolean = True


class Answer(models.Model):
    """Вариант ответа на вопрос"""
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    votes = models.IntegerField(verbose_name="Голосов", default=0)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
