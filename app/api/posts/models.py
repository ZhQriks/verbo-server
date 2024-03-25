from django.db import models
from app.utils.base_model import BaseModel

class Post(models.Model):
    explanation = models.TextField()
    mediaUrl = models.URLField(max_length=200)
    transcript = models.TextField(blank=True, null=True)
    isPhoto = models.BooleanField(default=False)
    viewCount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.explanation} - Group {self.mediaUrl}"

    def create_post(self, validated_data):
        class_instance = self.model(**validated_data)
        class_instance.save()
        return class_instance
