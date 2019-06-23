from django.urls import path

from .import views
app_name = ('app')

urlpatterns = [
	path('',views.home, name ='home'),
	path('room/',views.kotha,name = 'room'),
	path('room/<int:detail_id>/',views.room_detail, name ='detail')
]