from django.urls import path
from . import views

app_name = 'presentation'

urlpatterns = [
    path('download/', views.download_presentation, name='download'),
]
