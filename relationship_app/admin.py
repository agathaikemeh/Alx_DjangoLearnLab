from django.contrib import admin
from .models import UserProfile

# Register UserProfile model with admin interface
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Display the 'user' and 'role' fields in the admin interface
    search_fields = ('user__username', 'role')  # Add search functionality for username and role fields
    list_filter = ('role',)  # Add filter by role in the admin interface
    ordering = ('role',)  # Optionally, order by role field
