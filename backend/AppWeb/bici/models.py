from django.db import models

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

class Location(models.Model):
	class Meta:
		verbose_name = 'ubicacion'
	latitude = models.FloatField('latitud')
	longitude = models.FloatField('longitud')			

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.latitude