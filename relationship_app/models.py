from django.db import models
from django.contrib.auth.models import User  # Import the User model

# Existing models
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# New model: UserProfile
class UserProfile(models.Model):
    # Linking the UserProfile model to Django's User model via a OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # Choices for the role field
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Automatically create or update the UserProfile when a user is created
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Assign a default role of 'Member' if no role is set (although the default is already in the model)
        UserProfile.objects.create(user=instance, role='Member')
    else:
        instance.profile.save()  # Use the `related_name='profile'` for clarity

