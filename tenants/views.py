from django.shortcuts import render
from rest_framework import generics
from tenants.models import Tenant
from tenants.serializers import TenantSerializer

# Create your views here.
class CreateTenant(generics.CreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
