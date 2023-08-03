from django import forms
from .models import Apply,Job


class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields='__all__'
        exclude=('job',)


class Job_add_form(forms.ModelForm):
  class Meta:
    model=Job
    fields='__all__'
    exclude=('owner',)