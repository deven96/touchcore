from django.shortcuts import render
from touchcore.rest.models import Company, Employee
from touchcore.rest.serializers import EmployeeSerializer, CompanySerializer
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Endpoint for managing employees
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lists all the companies
    """
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
