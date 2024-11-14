from django.contrib import admin
from .models import Book

# Customizing the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for author and publication year
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality for the title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the custom admin settings
admin.site.register(Book, BookAdmin)

