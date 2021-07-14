from time import strptime

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Question, Answer
import datetime


# Create your views here.
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'we_have_questions'

    def get_queryset(self):
        # """Return sorted questions"""
        # questions = Question.objects.order_by('-date_published')
        """Return filtered questions"""
        if datetime.datetime.now().hour < 11:
            questions = Question.objects.filter(date_published__date=datetime.date.today())
            return questions


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


def vote(request, poll_id):
    question = get_object_or_404(Question, pk=poll_id)
    if not question.is_active:
        return HttpResponse('Опрос снят с публикации')
    else:
        if request.POST.get('answer'):
            try:
                selected_answer = question.answer_set.get(pk=request.POST['answer'])
            except (question.answer_set.get(pk=request.POST['answer']).DoesNotExist,
                    UnicodeEncodeError,
                    ValueError):
                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': "Указан недопустимый ответ",
                })

            selected_answer.votes += 1
            selected_answer.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        else:
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "Вы не выбрали ответ.",
            })


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        results = Question.objects.all()
        return results


def result(request, poll_id):
    return HttpResponseRedirect(reverse('polls:results'))
