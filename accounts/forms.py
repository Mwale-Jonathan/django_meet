from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SignupForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].widget.attrs['autofocus'] = False

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class AccountUpdateForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'image']
