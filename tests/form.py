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
       