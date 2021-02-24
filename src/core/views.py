from django.http import JsonResponse
from django.shortcuts import render

# function based view to return the required data
def test_view(request):
    data = {
        'name': 'John',
        'age' : 23
    }
    return JsonResponse(data)
