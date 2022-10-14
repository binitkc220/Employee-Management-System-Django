from django.urls import path
from .views import employee, employee_update, employee_delete

urlpatterns = [
    path('',employee),
    path('employee_update/<int:id>',employee_update),
    path('employee_delete/<int:id>',employee_delete),
]
