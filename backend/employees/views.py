from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
PermissionError

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        profile = self.request.user.profile

        if profile.role =="platform_admin":
            return Employee.objects.select_related("company").all()
        
        if profile.company:
            return Employee.objects.select_related("company").filter(
                company=profile.company
            )
        
        return Employee.objects.none()
    
    def perform_create(self, serializer):
        profile = self.request.user.profile

        if profile.company:
            serializer.save(company=profile.company)
            return
        
        raise PermissionError("User must belong to a company to create employees.")
