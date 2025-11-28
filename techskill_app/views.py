from rest_framework import viewsets
from .models import TechSkill
from .serializers import TechSkillSerializer

class TechSkillViewSet(viewsets.ModelViewSet):
    queryset = TechSkill.objects.all()
    serializer_class = TechSkillSerializer
