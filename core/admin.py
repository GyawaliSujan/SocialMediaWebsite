from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount, UserPreferences,MarkSheetInformation

models_list = [Profile, Post, LikePost, FollowersCount, UserPreferences,MarkSheetInformation]

# Register your models here.
for model in models_list:
    admin.site.register(model)
