from rest_framework import serializers
from .models import Post

# this is a transformation between our Model in the data base into a json  
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =(
            'title',
            'description',
            'owner'
            )
            