from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm



from .models import Task


# Create your views here.


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    context_object_name = "task"
    template_name = "tasks/task_add.html"
    fields = ['title', 'description','due_date']
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description','due_date']
    context_object_name ="task"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('tasks:task_list')

    def get_queryset(self):
        base_qs = super(TaskUpdateView, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')
    context_object_name = "task"

    def get_queryset(self):
        base_qs = super(TaskDeleteView, self).get_queryset()
        return base_qs.filter(user=self.request.user)


## This should be broken out into a separate app
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('tasks:task_list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/signup.html', {'form':form})
