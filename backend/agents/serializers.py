# backend/agents/serializers.py

from rest_framework import serializers
from .models import Team, Agent

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    agents = AgentSerializer(many=True, read_only=True)
    agent_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Agent.objects.all(), write_only=True
    )

    class Meta:
        model = Team
        fields = ['id', 'name', 'agents', 'agent_ids']

    def create(self, validated_data):
        agent_ids = validated_data.pop('agent_ids', [])
        team = Team.objects.create(**validated_data)
        team.agents.set(agent_ids)
        return team

    def update(self, instance, validated_data):
        agent_ids = validated_data.pop('agent_ids', [])
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        instance.agents.set(agent_ids)
        return instance
