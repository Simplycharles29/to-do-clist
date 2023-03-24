from django.forms import ModelForm
from .models import Tasks

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        field = '__all__'
        exclude = ['user']