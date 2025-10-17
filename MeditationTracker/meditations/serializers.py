from rest_framework import serializers
from .models import MeditationSession

class MeditationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationSession
        fields = ['id', 'user', 'meditation_type', 'duration', 'notes', 'date', 'created_at']
        read_only_fields = ['user', 'date', 'created_at']
