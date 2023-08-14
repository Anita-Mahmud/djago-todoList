from django import forms
from todo.models import TaskModel
class TodoListForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle','taskDescription']