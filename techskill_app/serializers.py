from rest_framework import serializers
from .models import TechSkill

class TechSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechSkill
        fields = '__all__'
