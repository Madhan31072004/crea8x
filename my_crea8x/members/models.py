from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed password
    skills = models.TextField()  # Comma-separated skills

    def __str__(self):
        return self.username
