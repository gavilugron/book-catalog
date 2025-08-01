from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]




#from django.urls import re_path, include
#from .views import book_view, health_view

#app_name = 'api'

#urlpatterns = [
#    re_path(
#        r"^$", health_view, name='health'
#    ),
#    re_path(
#        r"^books/", book_view, name='books'
#    )
#]

