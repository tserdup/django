from django.shortcuts import render
from .models import Room
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
	return render(request,'homes.html')


def kotha(request):
	room = Room.objects.all()
	context = {'room':room}
	return render(request,'room.html',context)

def room_detail(request,detail_id):
	detail =Room.objects.get(pk=detail_id)
	context = {'detail':detail}
	return render(request,'detail.html',context)