from django.db import models
from django.urls import reverse

# Create your models here.
def upload_location(instance, filename):
	return ("%s/%s") %(instance.title, filename)

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	image = models.ImageField(
		upload_to=upload_location,
		null=True, 
		blank=True,  
		height_field="height_field", 
		width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	timestamp = models.DateField(auto_now=False, auto_now_add=True)
	update = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', kwargs={"id":self.id})