from django.urls import path
from . import views

urlpatterns = [
    path('export-report', views.export_report),
]
