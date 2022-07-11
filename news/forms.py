from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'phone_number','notice','data']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ім’я'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефону'
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'рррр-мм-дд гг:хх'
            }),
            'notice': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Повідомлення'
            }),
        }