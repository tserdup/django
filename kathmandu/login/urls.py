from django.urls import path

from .import views

app_name ='register'

urlpatterns = [
	path('login/',views.login_view,name='login'),
	path('create/',views.create,name ='create')
]