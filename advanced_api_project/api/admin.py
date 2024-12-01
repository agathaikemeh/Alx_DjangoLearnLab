from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Book

# Register the Author model with the Django admin site
# This allows the Author model to be managed via the admin interface
admin.site.register(Author)

# Register the Book model with the Django admin site
# This enables the management of Book instances in the admin panel
admin.site.register(Book)

