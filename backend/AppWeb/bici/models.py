from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
	class Meta:
		verbose_name = 'tienda'
	description = models.TextField('descripción', blank=True, null=True)
	address = models.CharField('dirección', max_length=100, blank=True, null=True)
	value_km = models.IntegerField('cantidad de km', blank=True, null=True)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.address

class Route(models.Model):
	class Meta:
		verbose_name = 'ruta'
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='usuario')
	distance = models.FloatField('km')			
	speed = models.FloatField('velocidad')			
				

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return str(self.id)	

class Location(models.Model):
	class Meta:
		verbose_name = 'ubicacion'
	route = models.ForeignKey(Route, related_name='routes', on_delete=models.CASCADE)
	latitude = models.FloatField('latitud')
	longitude = models.FloatField('longitud')			

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return str(self.latitude)
	