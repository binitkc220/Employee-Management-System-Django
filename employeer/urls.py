from django.urls import path
from .views import employeer, employeer_update, employeer_delete

urlpatterns = [
    path('',employeer),
    path('employeer_update/<int:id>',employeer_update),
    path('employeer_delete/<int:id>',employeer_delete),
]
