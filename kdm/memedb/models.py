from django.db import models

# Create your models here.

class Tag(models.Model):
	title = models.CharField(max_length=75)
	slug = models.SlugField(max_length=75, unique=True)

	def __str__(self):
		return self.slug

class Meme(models.Model):
	title = models.CharField(max_length=75)
	slug = models.SlugField(max_length=75, unique=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.slug
