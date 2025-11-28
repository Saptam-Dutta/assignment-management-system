import uuid
from django.db import models

class Semester(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    semester_name = models.CharField(max_length=255, unique=True)
    sem_code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.semester_name
