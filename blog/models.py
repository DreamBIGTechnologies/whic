from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=50, null=False)
	body = models.TextField(max_length=5000, null=False)
	date_published = models.DateTimeField()
	

def __str(self):
	return post.title
