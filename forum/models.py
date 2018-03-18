from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)