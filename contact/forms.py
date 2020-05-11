from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'title', 'email', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'my-input',
                    'placeholder': 'Your Name'
                }
            ),
            'title': forms.EmailInput(
                attrs={
                    'class': 'my-input',
                    'placeholder': 'Konu'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'my-input',
                    'placeholder': 'Your E-Mail'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'my-textarea',
                    'rows': 10,
                    'placeholder': 'Mesajınız'
                }
            ),
        }
