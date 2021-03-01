from django.http import JsonResponse
from django.shortcuts import render
from .serializers import PostSerializer 
from .models import Post 
#third party imports
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset= Post.objects.all()

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer


#the most abstract class for the view, there are many API Views (List, Create, destroy, ListCreate....)
# class PostListCreateView(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset= Post.objects.all()

# class PostView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView):
    
#     serializer_class = PostSerializer
#     queryset= Post.objects.all()

#     def get(self,request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#     #to achieve a task before saving the data, u have to override this methode in the mixins
#     # def perform_create(self, serializer):
#     #     #send a mail
#     #     serializer.save()
   

# class Test_view(APIView):
#     #to set authentication to the API
#     #FOR MORE AUTH METHODS CHECK THE DOCUMENTATION OF django-rest-auth & django-rest-knox 
#     permission_classes = (IsAuthenticated, )
#     # in the get method we need a query set and pass it to the serializer and in the arguments
#     # in case of getting more than one instance we need to set set many = True
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many = True)
#         return Response(serializer.data)
#     # in the post method we need to check if the data is valid and then we can save it 
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) 
#         return Response(serializer.errors)

# # function based view to return the required data
# def test_view(request):
#     data = {
#         'name': 'John',
#         'age' : 23
#     }
#     return JsonResponse(data)
#  # if we want to return another type of data like a list we add safe parameter in the return 
#  # arrgument and set it to False -----> return JsonResponse(data,safe= Flase)