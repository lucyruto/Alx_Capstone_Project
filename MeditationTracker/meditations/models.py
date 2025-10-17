from django.db import models
from django.contrib.auth.models import User

MEDITATION_TYPES = [
    ('mindfulness', 'Mindfulness'),
    ('breathing', 'Breathing'),
    ('body_scan', 'Body Scan'),
    ('mantra', 'Mantra'),
    ('gratitude', 'Gratitude'),
]

class MeditationSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meditation_type = models.CharField(max_length=50, choices=MEDITATION_TYPES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.meditation_type} ({self.duration} mins)"
