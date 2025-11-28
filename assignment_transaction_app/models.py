import uuid
from django.db import models

class AssignmentTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    obtained_marks = models.IntegerField(null=True, blank=True)
    candidate_submit_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    student = models.ForeignKey('student_app.Student', on_delete=models.CASCADE, related_name='submissions')
    assignment = models.ForeignKey('assignment_app.Assignment', on_delete=models.CASCADE, related_name='submissions')
    submitted_file = models.FileField(upload_to='submissions/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'assignment')

    def __str__(self):
        return f"{self.student.student_usn_no} - {self.assignment.assignment_code}"
