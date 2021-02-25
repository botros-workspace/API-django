from django.http import JsonResponse
from django.shortcuts import render
from .serializers import PostSerializer 
from .models import Post 
#third party imports
from rest_framework.response import Response 
from rest_framework.views import APIView

class Test_view(APIView):
    # in the get method we need a query set and pass it to the serializer and in the arguments
    # in case of getting more than one instance we need to set set many = True
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors)

# # function based view to return the required data
# def test_view(request):
#     data = {
#         'name': 'John',
#         'age' : 23
#     }
#     return JsonResponse(data)
#  # if we want to return another type of data like a list we add safe parameter in the return 
#  # arrgument and set it to False -----> return JsonResponse(data,safe= Flase)