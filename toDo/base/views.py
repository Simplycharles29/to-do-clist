from django.shortcuts import render, redirect
from .models import Tasks
from .form import TaskForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .regform import RegisterForm

# Create your views here.

def registerUser(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'base/login_register.html', {'form': form})

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is incorrect')

    return render(request, 'base/login_register.html', {'page': page})

def logoutUser(request):
    logout(request)
    return redirect('home')

def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    tasks = Tasks.objects.filter(name__icontains = q)
    task_count = Tasks.objects.filter(completed = False).count()
    context = {'tasks': tasks, 'task_count' : task_count}
    return render(request, 'base/index.html', context)

@login_required(login_url='login')
def Taskpage(request, pk):
    task = Tasks.objects.get(id=pk)
    context = {'task': task}
    return render(request, 'base/task.html', context)

@login_required(login_url='login')
def createTask(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'base/create.html', context)

@login_required(login_url='login')
def editTask(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/edit.html', {'form': form})

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Tasks.objects.get(id = pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'obj': task}
    return render(request, 'base/delete.html', context)