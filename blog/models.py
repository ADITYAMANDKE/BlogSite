from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#our website we will have users and posts
#making a post model
class Post(models.Model):
#creating fields
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)#putting paranthesis after now would have executed the function we just was to pass it
	author = models.ForeignKey(User,on_delete=models.CASCADE) # user can create many posts one to many relationship 
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})