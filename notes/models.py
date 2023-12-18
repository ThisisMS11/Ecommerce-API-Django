from django.db import models
from django.utils import timezone
from .managers import CustomNotesManager

class Notes(models.Model):
    created_by = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    objects = CustomNotesManager()
    
