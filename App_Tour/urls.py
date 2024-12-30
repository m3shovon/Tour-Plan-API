from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourProgramViewSet, ParticipantViewSet, ParticipantBudgetViewSet

router = DefaultRouter()
router.register(r'tour-programs', TourProgramViewSet, basename='tour-program')
router.register(r'participants', ParticipantViewSet, basename='participant')
router.register(r'participant-budgets', ParticipantBudgetViewSet, basename='participant-budget')

urlpatterns = [
    path('', include(router.urls)),
]
