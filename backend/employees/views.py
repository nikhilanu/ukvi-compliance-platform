from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from compliance.services import calculate_employee_compliance
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

    @action(detail=True, methods=['get'])
    def compliance(self, request, pk=None):
        employee = self.get_object()
        compliance_result = calculate_employee_compliance(employee)

        return Response(compliance_result)