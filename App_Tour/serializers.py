from rest_framework import serializers
from .models import TourProgram, Participant

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'tour', 'user', 'amount_paid']

class TourProgramSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = TourProgram
        fields = ['id', 'creator', 'title', 'location', 'start_date', 'end_date', 'expected_budget', 'current_budget', 'participants']
