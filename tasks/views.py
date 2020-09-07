from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *

#This is the view that renders the home page which i the list page
def  index(request):

    tasks = Task.objects.all()
    form = TaskForm(request.POST)
    #complete = tasks.complete.count()
    #pending = tasks.complete.count()-tasks.count()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    complete_task = tasks.filter(complete=True).count()
    pending_task  = tasks.filter(complete=False).count()


    

    context= {'tasks':tasks, 'form':form, 'complete':complete_task, 'pending':pending_task}

    return render(request, "tasks/list.html", context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    


    context= {'form':form}
    return render(request, 'tasks/update_task.html', context)

#This View is for deleting the task that has been created...
def deleteTask(request, pk):

    #This is how we query the data base to get the Item we want to delete
    item = Task.objects.get(id=pk)

    #We used a form in our tempate and the method was POST
    #So we are now checking  if the nethod is Post and deleting the item
    if request.method == 'POST':

        item.delete()

        #After the delete has been complete we now return home...
        return redirect("/")

    #This is the dectionary that stores the information that is to be rendered
    context= {'item':item}
    return render(request, 'tasks/delete.html', context)

def about(request):

    return render(request, "tasks/about.html")