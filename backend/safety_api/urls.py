from django.urls import path
from .views import health, dashboard, resources, internships, emergency_contacts, create_alert
urlpatterns=[path('api/health/',health),path('api/dashboard/',dashboard),path('api/resources/',resources),path('api/internships/',internships),path('api/contacts/',emergency_contacts),path('api/alerts/',create_alert)]
