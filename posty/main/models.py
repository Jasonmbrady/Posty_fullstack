from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=64)
    # Time/Date Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    text = models.TextField()
    poster = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    favorite_of = models.ManyToManyField(User, related_name="favorites")
    # Time/Date Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     text = models.TextField()
#     commenter = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
#     commented_post = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)
#     # Time/Date Stamps
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
