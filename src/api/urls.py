from django.contrib import admin
from django.urls import path, include 
from core.views import PostListView, PostCreateView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', PostListView.as_view(), name = "list"),
    path('create/', PostCreateView.as_view(), name = "create"),
    path('token', obtain_auth_token, name = 'token')
]
