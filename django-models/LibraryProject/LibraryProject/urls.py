from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Importing redirect
from relationship_app import views  # Adjust according to the actual views in your app

# Define your URL patterns here
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', lambda request: redirect('login')),  # Redirect root URL to login
    path('books/', views.list_books, name='list_books'),  # View for listing books
    path('library/<int:pk>/', include('relationship_app.urls')),  # Including app-specific URLs
    path('login/', views.LoginView.as_view(), name='login'),  # Login view
    path('logout/', views.LogoutView.as_view(), name='logout'),  # Logout view
 path('register/', views.register, name='register'),  # Correct
 # Register view
]
