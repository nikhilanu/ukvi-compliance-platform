from rest_framework import serializers

from .models import Employee
from compliance.services import calculate_employee_compliance

class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(
        source="company.name",
        read_only=True
    )
    compliance_score = serializers.SerializerMethodField()
    compliance_status = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            "id",
            "company",
            "company_name",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "job_title",
            "department",
            "work_location",
            "is_sponsored",
            "visa_type",
            "visa_expiry_date",
            "right_to_work_check_date",
            "cos_number",
            "soc_code",
            "salary",
            "weekly_hours",
            "compliance_score",
            "compliance_status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "company",
            "company_name",
            "full_name",
            "compliance_score",
            "compliance_status",
            "created_at",
            "updated_at",
        ]
    
    def get_compliance_score(self, obj):
        return calculate_employee_compliance(obj)["score"]

    def get_compliance_status(self, obj):
        return calculate_employee_compliance(obj)["status"]