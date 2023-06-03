from django.db import models
from django.conf import settings

# Create your models here.

class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)



class Room(models.Model):
    label = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room ,related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message
    