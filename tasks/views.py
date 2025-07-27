from django.shortcuts import get_object_or_404, render , redirect


from .models import Tasks



# function based views
def list_todo(request):
    tasks = Tasks.objects.all()
    return render(request,'tasks/todo.html',{'tasks':tasks})


def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        Tasks.objects.create(title=title)
        return redirect('/todo')
    




def edit_status(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task.complated = not task.complated
        task.save()
        return redirect('/todo')



def delete_todo(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/todo')





# class based views


from django.views.generic import ListView, CreateView, View
from django.urls import reverse_lazy



class TaskListView(ListView):
    model = Tasks
    template_name = 'tasks/todo.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Tasks
    fields = ['title']
    template_name = 'tasks/todo.html'

    success_url = reverse_lazy('todo')  






class TaskDeleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        task.delete()
        return redirect('todo')