# backend/agents/models.py

from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    available_roles = models.JSONField(default=list, blank=True)
    available_skills = models.JSONField(default=list, blank=True)
    avatar = models.ForeignKey(
        Avatar,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='agents'
    )
    image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    agents = models.ManyToManyField(Agent, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    data = models.JSONField(default=dict, blank=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
