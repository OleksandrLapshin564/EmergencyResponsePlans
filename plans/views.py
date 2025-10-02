from django.shortcuts import render

# Home page
def home(request):
    return render(request, "plans/home.html")

# Lecture pages
def lecture1(request):
    return render(request, "plans/lecture1.html")

def lecture2(request):
    return render(request, "plans/lecture2.html")

def lecture3(request):
    return render(request, "plans/lecture3.html")

# New lectures (Emergency Response content)
def first_aid(request):
    return render(request, "plans/first_aid.html")

def fire_safety(request):
    return render(request, "plans/fire_safety.html")

def flood_earthquake(request):
    return render(request, "plans/flood_earthquake.html")
def disaster_preparedness(request):
    return render(request, "plans/disaster_preparedness.html")

def evacuation_plans(request):
    return render(request, "plans/evacuation_plans.html")

def emergency_contacts(request):
    return render(request, "plans/emergency_contacts.html")

