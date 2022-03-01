from tkinter import Label
from django import forms

class NewsLetterForm(forms.Form):
     your_name = forms.CharField(label='First Name',max_length=20)
     email = forms.EmailField(Label='Email')
