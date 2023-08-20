from django import forms
from .models import *


class Form_Test(forms.ModelForm):
    class Meta:
        model=Test
        fields='__all__'

class Form_SubTest(forms.ModelForm):
    class Meta:
        model=SubTest
        fields='__all__'
        exclude=('test_name',)
       
class Form_Patient(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'
        
       
class Form_Check(forms.ModelForm):
    class Meta:
        model=Check
        fields=['p_name','test_name','check_total']
    test_name= forms.ModelMultipleChoiceField(
        queryset=Test.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    p_name=forms.ModelChoiceField(
        queryset=Patient.objects.filter().order_by('-id'),
        widget=forms.Select
    )
        

class Form_Check_items(forms.ModelForm):
    class Meta:
        model=Check_items
        fields='__all__' 
        exclude=('check_id',)     
  