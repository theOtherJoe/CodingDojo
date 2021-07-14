from django.db import models
import re
from datetime import datetime, date

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        email_exists = User.objects.filter(email=(postData['email']))
        username_exists = User.objects.filter(user_name=(postData['user_name']))

        now = datetime.now()
        today = date.today()
        date_input = postData['birthday']
        final_date = datetime.strptime(date_input, "%Y-%m-%d")
        age = today.year - final_date.year - ((today.month, today.day) < (final_date.month, final_date.day))

        if email_exists:
            errors['email_exists'] = "Whoops, looks like that email is already being used! Try a different one."
        if username_exists:
            errors['username_exists'] = "Looks like that username is taken! Try something different!"
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to have at least 2 characters or more"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to have at least 2 characters or more"
        if len(postData['user_name']) < 2:
            errors['user_name'] = "User name needs to have at least 2 characters or more"
        if final_date.date() >= now.date():
            errors['birthday'] = "You must enter your birthday and it must be in the past"
        if age < 13:
            errors['age_check'] = "Sorry, you must be 13 or older to register!"
        if not email_check.match(postData['email']):
            errors['email'] = "Oops, invalid email address! Try again"
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 character or more"
        if postData['password'] != postData['confirm_password']:
            errors['password_match'] = "Oops, passwords don't match! Try again"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()