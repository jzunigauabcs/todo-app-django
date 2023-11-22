from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Task
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    tareas_completadas = list(filter(lambda t: (t.complete == 1), tasks))
    context = { "tasks":tasks, "tareas_completadas": len(tareas_completadas)}
    template = "task/index.html"
    return render(request, template, context)

def save_task(request):
    task = request.POST.get("txtTask", "")
    if task:
        t = Task(task=task)
        t.save()
    
    return redirect("/tasks")

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect("/tasks")

def complete_task(request, task_id):
    Task.objects.filter(id=task_id).update(complete=1)
    return redirect("task:index")
