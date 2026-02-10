from django.urls import path
from .views import fallen_list, memory_page

urlpatterns = [
    path("", memory_page, name="memory_index"),
    path("api/fallen/", fallen_list),
]
