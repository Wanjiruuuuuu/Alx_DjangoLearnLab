from django.db import models 
from django.contrib.auth.models import User  

class Patient(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    phone_number = models.CharField(max_length=15)  

    def __str__(self):  
        return self.user.username  

class MedicalRecord(models.Model):  
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  
    record_type = models.CharField(max_length=100)  
    data = models.JSONField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return f"{self.patient.user.username} - {self.record_type}"  
