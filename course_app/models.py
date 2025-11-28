import uuid
from django.db import models

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=255, unique=True)
    course_code = models.CharField(max_length=255, unique=True)
    org = models.ForeignKey('org_app.Org', on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.course_name
