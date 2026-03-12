from django.contrib import admin 
from django.urls import path
from .views import TaskLeastView, TaskCreateview

urlpatterns = [
    path("", TaskLeastView.as_view(), name = "task_list"),
    path("create/", TaskCreateview.as_view(), name =  "task_create" ), 
]