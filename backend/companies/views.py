from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        profile = self.request.user.profile

        if profile.role == "platform_admin":
            return Company.objects.all()

        if profile.company:
            return Company.objects.filter(id=profile.company.id)
        
        return Company.objects.none()
