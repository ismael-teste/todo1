from django.urls import path
from .views import list, updateTask, deleteTask


urlpatterns = [
    path("",list, name="list"),
    path("update/<int:pk>", updateTask, name="update"),
    path("delete/<int:pk>", deleteTask, name="delete"),
]
