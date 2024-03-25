from app.api.posts.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = Post
        fields = [
            'id',
            'explanation',
            'mediaUrl',
            'transcript',
            'isPhoto',
            'viewCount',
        ]

    def create_classroom(self, validated_data):
        return Post.objects.create_classroom(**validated_data)
