from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    sponsor_licence_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    industry = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    address = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ["name"]

    def __str__(self):
        return self.name