from django.urls import path
from . import views
urlpatterns = [
    path("", views.hash_functions, name="hash_functions"),
    path("ajax_hash_functions", views.ajax_hash_functions, name="ajax_hash_functions"),
    
]