from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),

    path("hash_functions", views.hash_functions, name="hash_functions"),
    path("ajax_hash_functions", views.ajax_hash_functions, name="ajax_hash_functions"),
    
    path("merkle_trees", views.merkle_trees, name="merkle_trees"),
    path("ajax_merkle_trees", views.ajax_merkle_trees, name="ajax_merkle_trees"),

    path("ajax_mining_simulation", views.ajax_mining_simulation, name="ajax_mining_simulation"),
    path("mining_simulation", views.mining_simulation, name="mining_simulation"),
    
]