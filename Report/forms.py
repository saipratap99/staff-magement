from django import forms
from .models import Staff

class AddStaffForm(forms.ModelForm):
  # staff_name = forms.CharField(max_length=100)
  # designation = forms.CharField(max_length=100)
  # salary = forms.DecimalField()
  class Meta:
    model = Staff
    fields = ['staff_name','designation','salary']
