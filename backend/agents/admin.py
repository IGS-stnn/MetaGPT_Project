# backend/agents/admin.py

from django.contrib import admin
from .models import Agent, Team, Template, Avatar

admin.site.register(Agent)
admin.site.register(Team)
admin.site.register(Template)
admin.site.register(Avatar)
