from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404

from .models import Question, Choice


# /polls/index/
def index(request):
    #
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context是一个由(变量名, python对象)组成的字典
    # 变量名对应html模板中的名称
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.htm', {'question': question})


def results(request, question_id):
    response = "you're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did'n select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(request.id,)))


