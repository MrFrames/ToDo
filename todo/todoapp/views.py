# detailed code commented out below.
from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import *
from django.template import loader
'''
# Create your views here.


def index (request):
    task_list = Task.objects.all()
    context = {'task_list':task_list}
    output = ','.join([q.task_priority for q in task_list])
    return render (request,'todoapp/index.html',context)

def newpage (request):
    return HttpResponse('This is a new page')

def detail (request, task_id):
    try:
        task = Task.objects.get(pk = task_id)
    except Task.DoesNotExist:
        raise Http404('Task with id={} does not exist.'.format(task_id))
    context = {
        'task' : task
    }
    return render(request,'todoapp/detail.html',context)
'''

from django.views import generic
from .models import Task

class IndexView (generic.ListView):
    template_name = 'todoapp/index.html'

    def get_queryset(self):
        return Task.objects.all()

class DetailView (generic.DetailView):
    model = Task
    template_name = 'todoapp/detail.html'

def UpdatedIndex(request,task_id):
    return HttpResponse("welcome to the updated index page: {}".format(task_id))

def UpdateView (request, task_code):
    task_list = Task.objects.all()
    task_list[task_code].done()
    context = {
        task_list: 'object_list'
    }
    return render(request,'todoapp/index.html',context)
