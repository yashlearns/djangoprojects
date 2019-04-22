from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Entry


class SignUpForm(UserCreationForm):
	email=forms.EmailField()
	first_name=forms.CharField(max_length=100)
	last_name=forms.CharField(max_length=100)
	fav_color=forms.CharField(max_length=100)

	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password1','password2')


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'What\'s on your mind?'})