from django.urls import path

from . import views

app_name = "task"
urlpatterns = [
    path("", views.index, name="index"),
    path("save/", views.save_task, name="save"),
    path("delete/<int:task_id>/", views.delete_task, name="delete"),
    path("complete/<int:task_id>/", views.complete_task, name="complete"),
]
