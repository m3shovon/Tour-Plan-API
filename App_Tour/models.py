from django.db import models
from App_Auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class TourProgram(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tours')
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    expected_budget = models.DecimalField(max_digits=10, decimal_places=2)
    current_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title

class Participant(models.Model):
    tour = models.ForeignKey(TourProgram, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=255) 
    email = models.EmailField(null=True, blank=True)  
    total_share = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            total_participants = self.tour.participants.count() + 1 
            self.total_share = self.tour.expected_budget / total_participants
            # total_share for existing participants
            for participant in self.tour.participants.all():
                participant.total_share = self.tour.expected_budget / total_participants
                participant.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.tour.title}"

class ParticipantBudget(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.participant.name}"

@receiver(post_save, sender=ParticipantBudget)
def update_participant_and_tour_budget(sender, instance, **kwargs):
    participant = instance.participant
    tour = participant.tour

    # Participant's amount_paid
    participant.amount_paid = participant.payments.aggregate(total=models.Sum('amount'))['total'] or 0
    participant.save()

    # TourProgram's current_budget
    tour.current_budget = tour.participants.aggregate(total=models.Sum('amount_paid'))['total'] or 0
    tour.save()