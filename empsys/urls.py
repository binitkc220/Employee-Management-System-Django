from django.contrib import admin
from django.urls import path, include
from .views import indexpage, dashboard
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexpage),
    path('employee/',include('employee.urls')),
    path('employeer/',include('employeer.urls')),
    path('accounts/',include('accounts.urls')),
]
