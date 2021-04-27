from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['username']) < 4:
            errors['username'] = "Usernames must be at least 4 characters long"
        elif len(User.objects.filter(username=postData['username'])) > 0:
            errors['username'] = "That username is taken"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif postData['password'] != postData['confirm_pass']:
            errors['password'] = "Passwords don't match"
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(username = postData['username'])
        if user:
            this_user = user[0]
            if postData['password'] != this_user.password:
                errors['password'] = "Invalid login credentials"
        else:
            errors['password'] = "Invalid login credentials"
        return errors


class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    # Time/Date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()