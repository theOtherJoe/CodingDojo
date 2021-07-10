from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def show_validator(self, postData):
        now = datetime.now()
        date_input = postData['release_date']
        final_date = datetime.strptime(date_input, "%Y-%m-%d")

        already_exists = Show.objects.get(title__exact=(postData['title']))
        errors = {}
        if already_exists:
            errors['exists'] = "Oops, that title already exists! Try a different one."
        if len(postData['title']) < 2:
            errors['title'] = "Title for the show must be at least 2 or more characters long."
        if final_date.date() >= now.date():
            errors['release_date'] = "You must provide a release date for the movie and it must be in the past."
        if len(postData['network']) < 3:
            errors['network'] = "You must provide a network for the show that must be 3 or more characters long."
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['description'] = "Description must be 10 or more characters long."
        return errors
class Network(models.Model):
    name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=75)
    release_date = models.DateField()
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()