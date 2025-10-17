from django.db import models
from django.conf import settings

MEDITATION_TYPES = [
    ('mindfulness', 'Mindfulness'),
    ('breathing', 'Breathing'),
    ('body_scan', 'Body Scan'),
    ('mantra', 'Mantra'),
    ('gratitude', 'Gratitude'),
]

class MeditationSession(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meditation_sessions'
    )
    meditation_type = models.CharField(max_length=50, choices=MEDITATION_TYPES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.meditation_type} ({self.duration} mins)"
