from django.shortcuts import render
from django.http import HttpResponse

# Home page view
def home(request):
    return HttpResponse("<h1>Welcome to Emergency Response Plans</h1>"
                        "<p>This is your first page!</p>")
