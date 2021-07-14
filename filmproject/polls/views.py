from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Question, Answer


# Create your views here.
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        """Вернуть 2 последних свежих опроса"""
        return Question.objects.order_by('-date_published')[:2]


# class QuestionDetailView(DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# def vote(request, poll_id):
#     question = get_object_or_404(Question, pk=poll_id)
#     if not question.is_active:
#         return HttpResponse('Опрос снят с публикации')
#     else:
#         if request.POST.get('answer'):
#             try:
#                 selected_answer = question.answer_set.get(pk=request.POST['answer'])
#             except (question.answer_set.get(pk=request.POST['answer']).DoesNotExist,
#                     UnicodeEncodeError,
#                     ValueError):
#                 return render(request, 'polls/detail.html', {
#                     'question': question,
#                     'error_message': "Указан недопустимый ответ",
#                 })
#
#             selected_answer.votes += 1
#             print(selected_answer.votes)
#             selected_answer.save()
#             return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#         else:
#             return render(request, 'polls/detail.html', {
#                 'question': question,
#                 'error_message': "Вы не выбрали ответ.",
#             })
#
#
# class ResultsView(DetailView):
#     model = Question
#     template_name = 'polls/results.html'
