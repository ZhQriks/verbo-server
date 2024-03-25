from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from app.api.posts.serializers import PostSerializer
from app.api.posts.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated

class PostViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(detail=False, methods=["post"])
    def create_post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            if post:
                return Response({'message': 'Classroom schedule created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def get_posts(self, request):
        posts = Post.objects.all()

        class_serializer = PostSerializer(posts, many=True)
        return Response(class_serializer.data)

    @action(detail=True, methods=["get"])
    def get_post(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        class_serializer = PostSerializer(post)
        return Response(class_serializer.data)
