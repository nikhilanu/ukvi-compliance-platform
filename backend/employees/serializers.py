from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(
        source="company.name",
        read_only=True
    )

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
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "company",
            "company_name",
            "full_name",
            "created_at",
            "updated_at",
        ]