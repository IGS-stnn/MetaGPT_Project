# backend/agents/admin.py

from django.contrib import admin
from .models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
