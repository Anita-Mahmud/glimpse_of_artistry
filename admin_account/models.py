from django.contrib.auth.models import User
from django.db import models

class Projects(models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='photos/projects')
    technologies = models.CharField(max_length=100)
    project_url = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    
    

class Resume(models.Model):
    resume = models.FileField(upload_to='resumes/')
    
class Skillset(models.Model):
    
    title = models.CharField(max_length=100, unique=True)
    level = models.CharField(max_length=100)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    message = models.TextField()
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
class Rating(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.PositiveIntegerField()