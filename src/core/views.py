from django.http import JsonResponse
from django.shortcuts import render

#third party imports
from rest_framework.response import Response 
from rest_framework.views import APIView

class Test_view(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        'name': 'John',
        'age' : 23
        }
        return Response(data)

# # function based view to return the required data
# def test_view(request):
#     data = {
#         'name': 'John',
#         'age' : 23
#     }
#     return JsonResponse(data)
#  # if we want to return another type of data like a list we add safe parameter in the return 
#  # arrgument and set it to False -----> return JsonResponse(data,safe= Flase)