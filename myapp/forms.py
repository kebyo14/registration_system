from django import forms
from django import forms
from .models import Forms  # Исправленный импорт

class ContactForm(forms.ModelForm):
    class Meta:
        model = Forms  # Теперь модель правильно указана
        fields = ['name', 'phone']

