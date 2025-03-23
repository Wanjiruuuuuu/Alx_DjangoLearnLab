from django.shortcuts import render
from rest_framework import generics  
from .models import Patient, MedicalRecord  
from .serializers import PatientSerializer, MedicalRecordSerializer  

class PatientListCreate(generics.ListCreateAPIView):  
    queryset = Patient.objects.all()  
    serializer_class = PatientSerializer  

class MedicalRecordListCreate(generics.ListCreateAPIView):  
    queryset = MedicalRecord.objects.all()  
    serializer_class = MedicalRecordSerializer  
