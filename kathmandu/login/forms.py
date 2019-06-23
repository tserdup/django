from django import forms
from django.contrib.auth.models import User
class UserRegistrationForm(forms.modeForm):
	firstname = forms.CharField(max_length=100,widget =forms.TextInput(attrs={'class':'input'}))
	lastname = forms.CharField(max_length=100,widget =forms.TextInput(attrs={'class':'input'}))
	username = forms.CharField(max_length=100,widget =forms.TextInput(attrs ={'class':'input'}))
	password = forms.CharField(max_length =100,widget =forms.PasswordInput(attrs={'class':'input'}))
	confirm = forms.CharField(max_length=100,widget =forms.PasswordInput(attrs ={'class':'input'}))
	class Meta:
		model = User
		fields = ['firstname','lastname','username','password','confirm']
