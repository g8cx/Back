from django.urls import path
from . import views

app_name = "memory"

urlpatterns = [
    path("", views.memory_page, name="memory_index"),
    path("add-fallen/", views.add_fallen, name="add_fallen"),
    path("api/fallen/", views.fallen_list, name="fallen_list"),
]