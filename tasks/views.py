from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Task


# Create your views here.
def index(request):
    list_of_tasks= Task.objects.all()
    context = {'list_of_tasks':list_of_tasks}
    return render(request, 'index.html', context)

def edit(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    response = "task %s bearbeiten"
    return HttpResponse(response % id)



def imprint(request):
    return render(request, 'imprint.html')

def add(request):
    return HttpResponse("you are at add")