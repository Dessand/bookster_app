from rest_framework import serializers
from ..models import Post

class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fileds = (
			'id',
			'title',
			'body',
			'author',
			'total_likes'
			)