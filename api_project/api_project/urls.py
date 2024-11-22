from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the API. Navigate to /api/books/ to see the book list.")

urlpatterns = [
    path('', index),  # Root path
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Includes api app URLs
]


