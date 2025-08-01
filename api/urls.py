from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import health_view

app_name = 'api'

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('health/', health_view, name='health'),
    path('', include(router.urls)),
]
