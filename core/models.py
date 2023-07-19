from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    
class UserPreferences(models.Model):
    favourite_cusine = models.CharField(max_length=50, null=True)
    favourite_sports = models.CharField(max_length=50, null=True)
    favourite_book = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.favourite_cusine
    
from django.db import models

class MarkSheetInformation(models.Model):
    CHOICE_OPTIONS = (
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Below Average', 'Below Average'),
    )
    user_name = models.CharField(max_length=20)
    math_marks = models.IntegerField()
    english_marks = models.IntegerField()
    teacher_marks = models.CharField(max_length=20, choices=CHOICE_OPTIONS)
    
    
    def __str__(self):
        self.user_name

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
