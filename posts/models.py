from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like

class Post(models.Model):
	
	title = models.CharField(max_length = 255)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		)
	likes = GenericRelation(Like)
	def __str__(self):

		return self.title

	def get_absolute_url(self):

		return reverse('post-detail', args=[str(self.id)])

	@property
	def total_likes(self):
		return self.likes.count()

# Create your models here.
