from rest_framework import viewsets, permissions
from django.db.models import Sum, Count
from django.contrib.auth import get_user_model
from .models import MeditationSession
from .serializers import MeditationSessionSerializer


User = get_user_model()

class MeditationSessionViewSet(viewsets.ModelViewSet):
    serializer_class = MeditationSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MeditationSession.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        session = serializer.save(user=self.request.user)
        self.update_consistency(self.request.user)
        self.check_leaderboard(self.request.user)

    def perform_destroy(self, instance):
        user = instance.user
        instance.delete()
        self.update_consistency(user)

    def update_consistency(self, user):
        total_sessions = MeditationSession.objects.filter(user=user).count()
        user.consistency_score = total_sessions
        user.save(update_fields=['consistency_score'])

    