from django.db import models
from django.utils import timezone
# from .managers import CustomNotesManager
from users.models import CustomUser
from django.contrib.postgres.fields import ArrayField

class CustomNotesManager(models.Manager):
    def create_note(self, content, tags, user=None):
        if not content:
            raise ValueError("content must be present")

        note = self.model(content=content, user=user)
        if tags:
            note.tags = tags

        note.save(using=self._db)
        
        # Handle the tags field
            
        return note


class Notes(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="notes",
        blank=True,
        null=False,
    )
    content = models.CharField(max_length=200)
    tags = ArrayField(
        models.CharField(max_length=10, blank=True),
        size=8
    )
    date_created = models.DateTimeField(default=timezone.now)

    objects = CustomNotesManager()

    def __str__(self) -> str:
        return self.content
