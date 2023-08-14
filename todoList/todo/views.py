from django.shortcuts import render,redirect
from .models import TaskModel
from .forms import TodoListForm
from django.views.generic import TemplateView,ListView,DeleteView,UpdateView,RedirectView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    
class StoreView(CreateView):
    model = TaskModel
    template_name = 'store.html'
    form_class = TodoListForm
    success_url = reverse_lazy('show')
    
class ShowView(ListView):
    model = TaskModel
    template_name = 'show.html'
    #context_object_name = 'data'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = TaskModel.objects.filter(is_completed = False)
        return context
    
class DeleteTaskView(DeleteView):
    model = TaskModel
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('show')
    
class EditView(UpdateView):
    model = TaskModel
    template_name = 'store.html'
    form_class = TodoListForm
    success_url = reverse_lazy('show')
    
class CompleteView(ListView):
    model = TaskModel
    template_name = 'complete_tasks.html'
    #context_object_name = 'data'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = TaskModel.objects.filter(is_completed = True)
        return context
    
class CompletedTaskView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        context = TaskModel.objects.get(pk=kwargs['pk'])
        context.is_completed = True
        context.save()
        return reverse_lazy('complete')
    


