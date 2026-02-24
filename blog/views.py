from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView,GenericAPIView
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.permissions import AllowAny

from .serializers import PostSerializer
from .models import Post

class PostList(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        posts = Post.objects.all()
        search = request.query_params.get('search')

        if search:
            print("Search VALUE"+ search)
            posts = posts.filter(title__icontains=search)

        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        many = isinstance(request.data,list)
        serializer = PostSerializer(data=request.data,many=many)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# ------- APIVIEW DETAIL --------    
    
class PostDetail(APIView):
    def get(self,request,slug):
        post = get_object_or_404(Post,slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self,request,slug):
        post = get_object_or_404(Post,slug=slug)
        serializer = PostSerializer(post,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# ------- CONCRETE GENERICVIEW DETAIL --------   

# class PostDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'slug'

# -------  GENERICVIEW + MIXINS DETAIL --------   

# class PostDetail(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'slug'

#     def get(self,request,slug):
#         return self.retrieve(request)
    
#     def put(self,request,slug):
#         return self.update(request)

#     def patch(self,request,slug):
#         return self.partial_update(request)
    
#     def delete(self,request,slug):
#         return self.destroy(request)
    