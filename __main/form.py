from django import forms
from __contact .models import News_letter

class Newsletter(forms.ModelForm):
    class Meta:
        model=News_letter
        fields='__all__'