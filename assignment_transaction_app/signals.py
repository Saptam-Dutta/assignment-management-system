from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AssignmentTransaction
from django.utils import timezone


@receiver(post_save, sender=AssignmentTransaction)
def set_submit_date(sender, instance, created, **kwargs):
    """
    Auto-update submit_datetime when new submission is created
    """
    if created and not instance.candidate_submit_date:
        instance.candidate_submit_date = timezone.now()
        instance.save(update_fields=["candidate_submit_date"])
