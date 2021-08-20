from django.db import models
import re
from datetime import datetime, date

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        email_exists = User.objects.filter(email=(postData['email']))

        now = datetime.now()
        today = date.today()
        date_input = postData['birthday']
        final_date = datetime.strptime(date_input, "%Y-%m-%d")
        age = today.year - final_date.year - ((today.month, today.day) < (final_date.month, final_date.day))

        if email_exists:
            errors['email_exists'] = "Whoops, looks like that email is already being used! Try a different one."
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to have at least 2 characters or more"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to have at least 2 characters or more"
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

class OrderManager(models.Manager):
    def order_validator(self, postData):
        errors = {}
        if postData['type_of_event'] == "default" or not postData['type_of_event']:
            errors['type_of_event'] = "Oops, you need to choose an event type!"
        if not postData['num_of_people'] or len(postData['num_of_people']) < 0:
            errors['num_of_people'] = "Number of people to serve must provided and more than 0"
        if postData['flavor'] == "default" or not postData['flavor']:
            errors['flavor'] = "Oops, don't forget to choose a flavor!"
        if postData['cb_selection'] == "default" or not postData['cb_selection']:
            errors['cb_selection'] = "Please make a cone or bowl selection!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birthday = models.DateField()
    password = models.CharField(max_length=50)
    bio = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # orders = []
    # flavors_liked = []

class Order(models.Model):
    type_of_event = models.CharField(max_length=50)
    num_of_people = models.IntegerField()
    flavor = models.CharField(max_length=50)
    cb_selection = models.CharField(max_length=50)
    orderer = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    special_requests = models.TextField()
    # total_cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrderManager()

class IceCream(models.Model):
    ic_flavor = models.CharField(max_length=50)
    description = models.CharField(max_length=75)
    price = models.IntegerField()
    users_who_like = models.ManyToManyField(User, related_name="flavors_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)