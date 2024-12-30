from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import TourProgram, Participant
from .serializers import TourProgramSerializer, ParticipantSerializer

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
