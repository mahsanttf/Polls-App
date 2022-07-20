# from django.shortcuts import render

# Create your views here.

# A view is a “type” of web page in your Django application - that generally serves a specific function and has a
# specific template. In Django, web pages and other content are delivered by views. Each view is represented by a
# Python function (or method, in the case of class-based views). Django will choose a view by examining the URL
# that’s requested (to be precise, the part of the URL after the domain name).

# Each view is responsible for doing one of two things: returning an HttpResponse object -
# containing the content for the requested page, or raising an exception such as Http404.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
from django.template import loader

# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#  This is the simplest view possible in Django. To call the view, we need to map it to a URL -
#  and for this we need a URLconf.
#  To create a URLconf in the polls directory, create a file called urls.py.

"""Raising a 404 error"""
"""
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question':question})
# A shortcut: get_object_or_404().
# It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist.
The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments,
which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist."""

'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
'''
'''
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #  Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
"""

"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))"""


'''def index(request):
    latest_question_list = Question.objects.order_by('id')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
'''
"""The render() function takes the request object as its first argument, a template name as its second argument
and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered
with the given context."""


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class ResultView(generic.ListView):
    template_name = 'polls/result.html'
    context_object_name = 'list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

