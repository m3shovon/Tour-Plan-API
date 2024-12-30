from rest_framework import serializers
from .models import TourProgram, Participant, ParticipantBudget

class ParticipantBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantBudget
        fields = ['id', 'participant', 'amount', 'payment_date']

class ParticipantSerializer(serializers.ModelSerializer):
    payments = ParticipantBudgetSerializer(many=True, read_only=True)

    class Meta:
        model = Participant
        fields = ['id', 'tour', 'name', 'email', 'total_share', 'amount_paid', 'payments']

class TourProgramSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = TourProgram
        fields = ['id', 'creator', 'title', 'location', 'start_date', 'end_date', 'expected_budget', 'current_budget', 'participants']
