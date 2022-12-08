from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'
class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwards={'pk':self.object.id})
class TaskDeleteView(DetailView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def add(request):
    task1=Task.object.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'task1':task1})