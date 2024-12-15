# Django Admin Integration for Book Model

## Steps to Integrate Book Model with Django Admin Interface:

1. **Register the Book Model**:
   - Open `bookshelf/admin.py`.
   - Add the following code to register the `Book` model:
     ```python
     from django.contrib import admin
     from .models import Book
     
     admin.site.register(Book)
     ```

2. **Customize the Admin Interface**:
   - Add a custom admin class to improve visibility and usability.
   - Modify `admin.py` as follows:
     ```python
     class BookAdmin(admin.ModelAdmin):
         list_display = ('title', 'author', 'publication_year')
         list_filter = ('author', 'publication_year')
         search_fields = ('title', 'author')
     
     admin.site.register(Book, BookAdmin)
     ```

3. **Testing the Admin Interface**:
   - Run the server: `python manage.py runserver`.
   - Visit `http://127.0.0.1:8000/admin` and login with your superuser credentials.
   - Ensure that the Book model displays the title, author, and publication year, and allows filtering and searching.

## Expected Outcome:
After completing these steps, the Book model should be fully integrated into the Django admin interface with enhanced display, filtering, and search capabilities.
