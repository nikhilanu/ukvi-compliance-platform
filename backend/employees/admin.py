from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "company",
        "job_title",
        "is_sponsored",
        "visa_type",
        "visa_expiry_date",
        "salary",
        "created_at",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "company__name",
        "cos_number",
        "soc_code",
    )
    list_filter = (
        "company",
        "is_sponsored",
        "visa_type",
    )