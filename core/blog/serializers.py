from django.forms import fields
from rest_framework import serializers
from .models import BlogCategory, Post

class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "author",
            "body",
            "likes",
            "write_date",
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
        )

class BlogCategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = BlogCategory
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "posts",
        )