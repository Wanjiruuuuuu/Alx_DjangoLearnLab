from django.urls import path  
from .views import PatientListCreate, MedicalRecordListCreate  

urlpatterns = [  
    path('patients/', PatientListCreate.as_view()),  
    path('records/', MedicalRecordListCreate.as_view()),  
]  