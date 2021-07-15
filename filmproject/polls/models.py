from django.db import models
import datetime
from django.contrib.auth.models import User
# Импортируем настройки приложения polls
from polls import settings


# Create your models here.
class Question(models.Model):
    """Вопрос"""
    title = models.CharField(max_length=128, verbose_name="Question")
    date_published = models.DateTimeField(default=datetime.datetime.now())
    is_active = models.BooleanField(default=True, verbose_name="Actual")

    def __str__(self):
        return self.title

    # Этот метод позволяет выявить Популярный опрос для показа в админке
    def is_popular(self):
        answers = Answer.objects.filter(question_id=self.id)
        votes_total = sum([answer.votes for answer in answers])
        return votes_total > settings.POLLS_POPULAR_VOTES_LIMIT

    # Описание столбца в админке
    is_popular.short_description = 'Popular'
    # Вот настройка, заменяющая False/True на иконки в админке
    is_popular.boolean = True


class Answer(models.Model):
    """Вариант ответа на вопрос"""
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=64, verbose_name="Answer")
    votes = models.IntegerField(verbose_name="Голосов", default=0)

    def __str__(self):
        return self.answer


class Description(models.Model):
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    string_desc = models.CharField(max_length=32, unique=False)
    digital_desc = models.DecimalField(decimal_places=2, default=0, max_digits=5)

    def __str__(self):
        return self.string_desc


class Participation(models.Model):
    """Пользователь, участвующий в опросе"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question')

    def __str__(self):
        return self.user.name

    def voted_already(self):
        """Голосовал ли пользователь в опросе"""
        user_list = Participation.objects.filter(user=self.user, question=self.question)
        return len(user_list) > 0

    class Meta:
        verbose_name_plural = 'Participation'
