from django.contrib import admin
from .models import Question, Answer


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
    list_display = ('title', 'date_published', 'is_active')


# Register your models here.
# Модель Answer импортировать не нужно, т.к. она связана с Question через внешний ключ.
admin.site.register(Question, QuestionAdmin)
