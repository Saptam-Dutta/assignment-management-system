from rest_framework import serializers
from .models import AssignmentTransaction

class AssignmentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentTransaction
        fields = "__all__"
        read_only_fields = ("created_at",)

    def validate(self, data):
        """
        Prevent duplicate submission for student + assignment.
        """
        student = data.get("student")
        assignment = data.get("assignment")

        if self.instance is None:
            if AssignmentTransaction.objects.filter(
                student=student, assignment=assignment
            ).exists():
                raise serializers.ValidationError(
                    "Student has already submitted this assignment!"
                )

        return data
