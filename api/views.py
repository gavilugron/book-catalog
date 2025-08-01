from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok"
        })

health_view = HealthView.as_view()

class BookViewSet(viewsets.ModelViewSet):
    """
    Provides list, create, retrieve, update and destroy actions for Book.
    """
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer