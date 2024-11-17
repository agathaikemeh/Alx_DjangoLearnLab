# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail
]
# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail
]
from django.urls import path, include

urlpatterns = [
    path('relationship/', include('relationship_app.urls')),
]
