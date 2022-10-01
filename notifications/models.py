from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):

    INFO = 'info'
    ERROR = 'err'
    SUCCESS = 'suc'

    type_choices = [
        (INFO, 'Information'),
        (ERROR, 'Erreur'),
        (SUCCESS, 'Success'),
    ]
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Receiver')
    message = models.TextField(verbose_name='message')
    type = models.CharField(max_length=255, verbose_name='Choices', choices=type_choices, default=INFO)
    created_at = models.DateField(auto_now_add=True)

class NotificationByUser(Notification):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Sender')