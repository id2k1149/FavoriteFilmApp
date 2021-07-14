from django.contrib import admin
from .models import Question, Answer, Description


# варианты ответа можно будет добавить на той же странице, что и вопрос опроса.
# class AnswerInline(admin.StackedInline):
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2


# Поменяем порядок полей в админке
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['is_active', 'date_published', 'title']

# Добавим филдсеты (fieldsets) – группы полей.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'is_active']}
         ),
        ('Информация о дате',
         {'fields': ['date_published'],
          'classes': ['collapse']}
         ),
    ]
    inlines = [AnswerInline]

    # неактивный опрос отображать не будем
    # Добавим название метода модели is_popular()
    list_display = ('title', 'date_published', 'is_active', 'is_popular')

    # в админке добавить фильтр по дате
    list_filter = ['date_published']

    # Добавим форму поиска по формулировкам вопросов
    search_fields = ['title']

    # Добавим в админку иерархию по дате: год, месяц…
    # нужно установить питоновский пакет pytz (PYthon TimeZone).
    # date_hierarchy = ['date_published']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Description)
