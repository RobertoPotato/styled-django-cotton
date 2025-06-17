from django.urls import path
from . import views

urlpatterns = [
    path('financial/', views.financial_report, name='reports_financial'),
    path('occupation/', views.occupation_report, name='reports_occupation'),
    path('property/', views.property_report, name='reports_property'),
]

