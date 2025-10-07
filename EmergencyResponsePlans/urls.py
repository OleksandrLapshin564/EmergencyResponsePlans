from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('presentation/', include('presentation.urls', namespace='presentation')),  # presentation app
    path('', include('plans.urls', namespace='plans')),  # home and lecture pages
]
