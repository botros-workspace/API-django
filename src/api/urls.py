from django.contrib import admin
from django.urls import path, include 
from core.views import Test_view

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', Test_view.as_view(), name = "test"),
    path('token', obtain_auth_token, name = 'token')
]
