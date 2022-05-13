from rest_framework.generics import ListCreateAPIView

from blogs.models import BlogPost
from blogs.serializers import BlogPostSerializer


class BlogPostAPIView(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer