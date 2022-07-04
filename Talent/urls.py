from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path("detailform/", views.TalentDetailsApi.as_view(), name="talent_detail"),
]