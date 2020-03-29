from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required 
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
        messages.success(request,("New task added"))
        return redirect('todolist')

    else:       
        all_tasks = TaskList.objects.filter(manager=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)


        return render(request, 'todolist.html' , {'all_tasks' : all_tasks})

def contact(request):
    context = {
        'Welcome_text' : "Welcome to Contact page",
    }
    return render(request, 'contact.html' , context)

@login_required
def delete_task(request, id):
    task = TaskList.objects.get(id = id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request,("You are not authorized"))


    return redirect('todolist')

@login_required
def complete_task(request, id):
    task = TaskList.objects.get(id = id)
    if task.manager == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,("You are not authorized"))

    return redirect('todolist')

@login_required
def pending_task(request, id):
    task = TaskList.objects.get(id = id)
    if task.manager == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request,("You are not authorized"))

    return redirect('todolist')

@login_required
def edit_task(request, id):
    if request.method == "POST":
        task = TaskList.objects.get(id = id)
        form = TaskForm(request.POST or None , instance = task)
        if form.is_valid():
            form.save()

       
        messages.success(request,("Task edited"))
        return redirect('todolist')

    else:       
        task_obj = TaskList.objects.get(id = id)
        return render(request, 'edit.html' , {'task_obj' : task_obj})


def index(request):
    context = {
        'index_text' : "Welcome to index page",
    }
    return render(request, 'index.html' , context) 

      

def about(request):
    context = {
        'Welcome_text' : "Welcome to about page",
    }
    return render(request, 'about.html' , context) 