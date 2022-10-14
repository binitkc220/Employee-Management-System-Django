from django.forms import ModelForm
from .models import employees

class EmployeerForm(ModelForm):
    class Meta:
        model = employees
        fields = ['full_name','address','email']
        