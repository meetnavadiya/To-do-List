from django.shortcuts import render ,redirect
from .models import Task

# Create your views here.

def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
       
        Task.objects.create(
            tname=name,
            tdesc=desc
        )
        return redirect('table')
    
    return render(request,'home.html')

def view(request,pk):

    tasks=Task.objects.get(id=pk)
    
    return render(request,'view.html',{'data':tasks})


def table(request):

    query=request.GET.get('q','')
    tasks=Task.objects.filter(tname__icontains=query)
    return render(request,'table.html',{'data':tasks})
   

def update_task(request,id):
    task=Task.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        task.tname=name
        task.tdesc=desc
        task.save()
        return redirect('table')
    
    return render(request,'update.html',{'data':task})


def delete_task(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('table')

