from . import models
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyDetails
        fields = "__all__"
