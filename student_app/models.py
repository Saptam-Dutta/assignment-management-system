import uuid
from django.db import models

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_usn_no = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20, blank=True)
    course = models.ForeignKey('course_app.Course', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.student_usn_no
