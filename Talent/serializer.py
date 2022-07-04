from . import models
from rest_framework import serializers


class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TalentDetails
        fields = "__all__"