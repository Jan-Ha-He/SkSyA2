import imp
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.forms.models import model_to_dict
import logging

from .models import Task


# Create your views here.
def index(request):
    if request.method == 'POST':
        #Task.objects.get(id=request.POST['deleteId']).delete()
        Task.objects.get(id=request.POST.get('deleteId')).delete()
        list_of_tasks= Task.objects.all()
        context = {'list_of_tasks':list_of_tasks}
    if request.method == 'GET':
        list_of_tasks= Task.objects.all()
        context = {'list_of_tasks':list_of_tasks}
    return render(request, 'index.html', context)

def edit(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    if request.method == 'POST':
        task.task_text = request.POST.get("description")
        task.deadline = request.POST.get("deadline")
        task.progress = request.POST.get("progress")
        task.save()
        list_of_tasks= Task.objects.all()
        context = {'list_of_tasks':list_of_tasks}
        return render(request, 'index.html', context)
    elif request.method == 'GET':
        context = {'task': task}
        date = task.deadline.strftime('%Y-%m-%d')
        context['date'] = date
        return render(request, 'edit.html', context)


def imprint(request):
    return render(request, 'imprint.html')


def add(request):
    if request.method == 'POST':
        task = Task.objects.create(task_text=request.POST.get(
            "description"), deadline=request.POST.get("deadline"), progress=request.POST.get("progress"))
        task.save()
        list_of_tasks= Task.objects.all()
        context = {'list_of_tasks':list_of_tasks}
        return render(request, 'index.html', context)
    elif request.method == 'GET':
        return render(request, 'add.html')
