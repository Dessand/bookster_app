from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from posts.models import Post
from .models import Like
from django.contrib.auth import get_user_model

class LikesTests(TestCase):

	def SetUp(self):
		
		self.user = get_user_model().objects.create_user(
			username = 'testuser1', password = 'password')

		self.post = Post.objects.create(
			title = 'makaka',
			body = 'dakaka',
			author = self.user,)

		self.post_model_type = ContentType.objects.get_for_model(post)
		
		self.like = Like.objects.create(
			content_type = post_model_type,
			object_id = self.post.id,
			user = self.user)

	def test_like_count(self):

		self.assertEqual(post.total_likes, 1)
		self.assertEqual(Like.objects.count(), 1)
		self.assertEqual(Like.objects.first().content_object, 'makaka')

# Create your tests here.
