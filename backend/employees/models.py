from django.db import models

# Create your models here.
from django.db import models

from companies.models import Company


class Employee(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="employees",
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    job_title = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    work_location = models.CharField(max_length=255, blank=True, null=True)

    is_sponsored = models.BooleanField(default=False)
    visa_type = models.CharField(max_length=100, blank=True, null=True)
    visa_expiry_date = models.DateField(blank=True, null=True)
    right_to_work_check_date = models.DateField(blank=True, null=True)

    cos_number = models.CharField(
        "Certificate of Sponsorship number",
        max_length=100,
        blank=True,
        null=True,
    )
    soc_code = models.CharField(
        "SOC code",
        max_length=50,
        blank=True,
        null=True,
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    weekly_hours = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.full_name