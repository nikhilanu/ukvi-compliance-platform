from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sponsor_licence_number",
        "industry",
        "created_at",
    )
    search_fields = (
        "name",
        "sponsor_licence_number",
        "industry",
    )
    list_filter = ("industry",)