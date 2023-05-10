from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from users.forms import *

# основная страница с задачами
def manepage(request):
    messages={}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if len(form['title'].value())<=30:
            Task.objects.create(user_id=(User.objects.get(username=request.user)).id,title=form['title'].value())
        else:
            messages = {'Название должно быть меньше 30 символов'}
    try:
        tasks = Task.objects.filter(user_id=(User.objects.get(username=request.user)).id)
    except:
        tasks=[]

    form = TaskForm()
    context = {'tasks': tasks, 'form': form,'messages': messages}
    return render(request, "users/task_list.html",context)

# вход
def log(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                form = TaskForm(request.POST)
                if form.is_valid():
                    form.save()
                tasks=Task.objects.filter(user_id=(User.objects.get(username=username)).id)
                form=TaskForm()
                context = {'tasks': tasks, 'form': form}
                return render(request,'users/task_list.html',context)

    messages = {'Имя пользователя или пароль некорректны'}
    return render(request, 'users/login.html', {'form': form,'messages':messages})


# регистрация
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'users/register.html', {'form': form})

# выход
def sign_out(request):
    logout(request)
    return redirect('task_list')

# удаление задач
def delete(request, id,username):
    task = Task.objects.get(id=id)
    task.delete()
    tasks = Task.objects.filter(user_id=(User.objects.get(username=username)).id)
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'users/task_list.html', context)

# изменение статуса (выполнено или нет)
def edit(request, id,username):
    task = Task.objects.get(id=id)
    if task.complete:
        task.complete=0
    else:
        task.complete=1
    task.save()
    tasks = Task.objects.filter(user_id=(User.objects.get(username=username)).id)
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'users/task_list.html', context)



