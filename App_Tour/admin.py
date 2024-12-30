from django.contrib import admin
from App_Tour.models import TourProgram, Participant, ParticipantBudget
# Register your models here.



admin.site.register(TourProgram)
admin.site.register(Participant)
admin.site.register(ParticipantBudget)
