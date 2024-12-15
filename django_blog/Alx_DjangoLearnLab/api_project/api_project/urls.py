from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token  # Import the token view

def root_view(request):
    return HttpResponse("Welcome to the API. Navigate to /api/books/ to see the book list.")

urlpatterns = [
    path('', root_view),  # Root path
    path('admin/', admin.site.urls),  # Admin site
    path('api/', include('api.urls')),  # Includes api app URLs
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),  # Token retrieval endpoint
]




