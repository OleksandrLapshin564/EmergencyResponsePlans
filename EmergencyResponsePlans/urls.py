"""
URL configuration for EmergencyResponsePlans project.
"""

from django.contrib import admin
from django.urls import path
from plans.views import home  # import our view for the main page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # home page
]
