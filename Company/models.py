from django.db import models
from user_module.models import CustomUsers


class CompanyDetails(models.Model):
    email = models.OneToOneField(CustomUsers, verbose_name="email", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)

    def __str__(self):
        return self.name
