from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path("detailform/", views.CompanyDetailsApi.as_view(), name="company_detail"),
]