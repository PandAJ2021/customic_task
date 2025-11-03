import uuid
from django.db import models
from django.conf import settings


class Mockup(models.Model):
    FONT_CHOICES = [
        ('courier', 'Courier'),
        ('great_vibes', 'Great Vibes'),
        ('lobster', 'Lobster'),
        ('opensans', 'Open Sans'),
        ('pacifico', 'Pacifico'),
        ('playfair', 'Playfair Display'),
        ('roboto', 'Roboto'),
        ('times', 'Times New Roman'),
        ('vermin', 'Vermin_Vibes'),
    ]

    SHIRT_COLOR_CHOICES = [
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('white', 'White'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mockups')
    font = models.CharField(max_length=50, choices=FONT_CHOICES)
    text = models.CharField(max_length=255)
    text_color = models.CharField(max_length=7, default='#000000')
    shirt_colors = models.JSONField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text_color} - {self.font} text on {', '.join(self.shirt_colors)} shirt(s)"
    
    def save(self, *args, **kwargs):
        if not self.shirt_colors:
            self.shirt_colors = list(choice[0] for choice in self.SHIRT_COLOR_CHOICES)
        return super().save(*args, **kwargs)


class Result(models.Model):
    mockup = models.ForeignKey(Mockup, on_delete=models.CASCADE, related_name='results')
    image_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.mockup.task_id} - {self.image_url}"