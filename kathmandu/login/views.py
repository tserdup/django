from django.contrib.auth import authenticate,login

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

# Create your views here.
def login_view(request):
	if request.method == "POST":
		username =request.POST['username']
		password =request.POST['password']
		user =authenticate(request,username = username, password = password)
		if user:
			return redirect('app:room')
	else:
		messages.error(request,'username or password is wrong')
	return render(request,'login.html')

def create(request):
	if request.method =="POST":
		create =UserRegistrationForm(request.POST)
		if create.is_valid():
			firstname = create.cleaned_data.get('firstname')
			lastname =create.cleaned_data.get('lastname')
			username = create.cleaned_data.get('username')
			password = create.cleaned_data.get('password')
			confirm = create.cleaned_data.get('confirm')
			user = User.objects.create_user(firstname,lastname,username,password,confirm)
			if user:
				return redirect('app:room')

	else:
		create = UserRegistrationForm()
		context ={'create':create}
		return render(request,'create.html',context)