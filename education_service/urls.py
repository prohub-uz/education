from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edu/', include('education.urls')),
    path('manager/', include('education.services.Admins.urls')),
]
