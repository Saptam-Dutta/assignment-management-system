import uuid
from django.db import models

class Assignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assignment_name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_marks = models.PositiveIntegerField()
    assignment_code = models.CharField(max_length=255, unique=True)

    course = models.ForeignKey('course_app.Course', on_delete=models.CASCADE, related_name='assignments')
    semester = models.ForeignKey('semester_app.Semester', on_delete=models.CASCADE, related_name='assignments')
    subject = models.ForeignKey('subject_app.Subject', on_delete=models.CASCADE, related_name='assignments')
    tech_skill = models.ForeignKey('techskill_app.TechSkill', on_delete=models.CASCADE, related_name='assignments')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assignment_name
