from django.conf import settings
from django.db import models

from companies.models import Company


class UserProfile(models.Model):
    ROLE_PLATFORM_ADMIN = "platform_admin"
    ROLE_EMPLOYER_ADMIN = "employer_admin"
    ROLE_EMPLOYEE = "employee"

    ROLE_CHOICES = [
        (ROLE_PLATFORM_ADMIN, "Platform Admin"),
        (ROLE_EMPLOYER_ADMIN, "Employer Admin"),
        (ROLE_EMPLOYEE, "Employee"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_profiles",
    )
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default=ROLE_EMPLOYEE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"