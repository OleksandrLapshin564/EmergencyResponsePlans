from django.urls import path
from . import views

app_name = "plans"

urlpatterns = [
    path("", views.home, name="home"),
    path("lecture1/", views.lecture1, name="lecture1"),
    path("lecture2/", views.lecture2, name="lecture2"),
    path("lecture3/", views.lecture3, name="lecture3"),
    path("first-aid/", views.first_aid, name="first_aid"),
    path("fire-safety/", views.fire_safety, name="fire_safety"),
    path("flood-earthquake/", views.flood_earthquake, name="flood_earthquake"),
    path("disaster-preparedness/", views.disaster_preparedness, name="disaster_preparedness"),
    path("evacuation-plans/", views.evacuation_plans, name="evacuation_plans"),
    path("emergency-contacts/", views.emergency_contacts, name="emergency_contacts"),

]
