from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.forms.models import model_to_dict

from .models import Task


# Create your views here.
def index(request):
    list_of_tasks= Task.objects.all()
    context = {'list_of_tasks':list_of_tasks}
    return render(request, 'index.html', context)

def edit(request, id):
    if request.method == 'POST':
        task =  Task.objects.get(id=id)
        task.description = request.POST.get("description")
        ##task.deadline = request.POST.get("deadline")
        task.progress = request.POST.get("progress")
        task.save()
        return render(request,'edit.html', {'task':task})
    elif request.method == 'GET':
        try:
            task =  Task.objects.get(id=id)

        except Task.DoesNotExist:
            raise Http404("Task does not exist")
        return render(request,'edit.html', {'task':task})


def imprint(request):
    return render(request, 'imprint.html')

def add(request):
    return HttpResponse("you are at add")