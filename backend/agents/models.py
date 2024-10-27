# backend/agents/models.py

from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    available_roles = models.JSONField(default=list)  # Список доступных ролей
    available_skills = models.JSONField(default=list)  # Список доступных навыков

class Team(models.Model):
    name = models.CharField(max_length=100)
    agents = models.ManyToManyField(Agent, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
