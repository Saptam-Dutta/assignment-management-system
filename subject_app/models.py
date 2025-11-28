import uuid
from django.db import models

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_name = models.CharField(max_length=255, unique=True)
    subject_code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.subject_name
