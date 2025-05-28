from django.db.models import Case, When, IntegerField
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'

    def get_queryset(self):
        priority_order = Case(
            When(priority='High', then=1),
            When(priority='Medium', then=2),
            When(priority='Low', then=3),
            output_field=IntegerField(),
        )
        return Task.objects.annotate(
            priority_order=priority_order
        ).order_by('priority_order', 'date')


class TaskDetailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model= Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
         return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model= Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', "")
        priority = request.POST.get('priority', '')
        status = request.POST.get('status', '')
        description = request.POST.get('description', "")
        date = request.POST.get('date', '')
        task = Task(
            name=name,
            priority=priority,
            date=date,
            description=description,
            status=status,
            user=request.user  # Assign the logged-in user
        )
        task.save()
        return redirect('/')  # Replace 'index' with your desired redirect
    return render(request, 'home.html', {'task1': task1})

#def details(request):
  #  return render(request,'detail.html')


def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect("/")
    return render(request,'edit.html',{'f':f,'task':task})
