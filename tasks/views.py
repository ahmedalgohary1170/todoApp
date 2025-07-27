from django.shortcuts import get_object_or_404, render , redirect


from .models import Tasks




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
