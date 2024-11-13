# backend/agents/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Agent, Template, Avatar

class AvatarSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Avatar
        fields = ['id', 'name', 'image', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None

class AgentSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(read_only=True)
    avatar_id = serializers.PrimaryKeyRelatedField(
        queryset=Avatar.objects.all(),
        source='avatar',
        write_only=True,
        required=False
    )

    class Meta:
        model = Agent
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    agents = AgentSerializer(many=True, read_only=True)
    agent_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Agent.objects.all(), write_only=True, source='agents'
    )

    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        agents = validated_data.pop('agents', [])
        team = Team.objects.create(**validated_data)
        team.agents.set(agents)
        return team

    def update(self, instance, validated_data):
        agents = validated_data.pop('agents', [])
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        if agents:
            instance.agents.set(agents)
        return instance

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user
