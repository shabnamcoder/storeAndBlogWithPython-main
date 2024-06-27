from unicodedata import category
from django.db.models import Q
from pydoc import describe
from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post, BlogCategory
from .serializers import PostSerializer, BlogCategorySerializer

# Create your views here.


class HeadPostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[:0]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class TopPostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[1:3]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class LatestPostsList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[3:6]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetail(APIView):
    def get_object(self, category_slug, product_slug, format=None):
        try:
            return BlogCategory.objects.filter(category_slug=category_slug)
        except BlogCategory.DoesNotExist:
            raise Http404
    
    def get(self,request, category_slug, post_slug, format=None ):
        posts = self.get_object(category_slug, post_slug)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

class BlogCategoryDetail(APIView):
    def get_object(self,category_slug):
        try:
            return BlogCategory.objects.get(slug=category_slug)
        except BlogCategory.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = BlogCategorySerializer(category)
        return Response(serializer.data)



@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        posts = Post.objects.filter(Q(title__icontains = query) | Q(body__icontains = query))
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    else:
        return Response({"posts":[]})

