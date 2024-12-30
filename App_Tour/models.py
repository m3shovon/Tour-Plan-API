from django.db import models
from App_Auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.name} - {self.tour.title}"
