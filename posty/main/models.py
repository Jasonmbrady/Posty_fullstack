from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]+$')
        if len(postData['name']) < 3:
            errors['name'] = "User names must be at least 3 characters long"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid e-mail address!"
        if len(postData['password']) < 8:
            errors['password'] = "Passwords must be 8+ characters"
        return errors

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=30, default="password")
    # Time/Date Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

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
