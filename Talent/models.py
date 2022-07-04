from django.db import models
from user_module.models import CustomUsers


# Create your models here.
class TalentDetails(models.Model):
    gender = {
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("NOT TO SAY", "NOT TO SAY")
    }
    email = models.OneToOneField(CustomUsers, verbose_name="email", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=gender, default="Not Selected")
    higher_educations = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.name
