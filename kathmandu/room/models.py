from django.db import models
from django.utils import timezone
# Create your models here.
class Room(models.Model):
	room = (
		('house','House'),
		('apartment','Apartment'),
		('room','Room'),
		('hostel','Hostel'),
	)

	District =models.CharField(max_length=100)
	City  = models.CharField(max_length= 50)
	Area = models.CharField(max_length =30)
	price = models.IntegerField()
	yourproperty = models.CharField(max_length =15,choices =room)
	img = models.ImageField(upload_to ='image')
	room = models.IntegerField()
	garden = models.BooleanField()
	water = models.IntegerField()
	date =models.DateTimeField(default=timezone.now)
	description = models.TextField()

