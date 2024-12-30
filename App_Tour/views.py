from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import TourProgram, Participant, ParticipantBudget
from .serializers import TourProgramSerializer, ParticipantSerializer, ParticipantBudgetSerializer

class TourProgramViewSet(ModelViewSet):
    queryset = TourProgram.objects.all()
    serializer_class = TourProgramSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ParticipantViewSet(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]

class ParticipantBudgetViewSet(ModelViewSet):
    queryset = ParticipantBudget.objects.all()
    serializer_class = ParticipantBudgetSerializer
    permission_classes = [IsAuthenticated]
