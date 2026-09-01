from django.urls import path

from my_apps.tasker import views

app_name = "tasker"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="list"),
    path("create/", views.CreateTaskView.as_view(), name="create"),
    path(
        "subtask/create/<int:task_id>/",
        views.CreateSubTaskView.as_view(),
        name="create_subtask",
    ),
]
