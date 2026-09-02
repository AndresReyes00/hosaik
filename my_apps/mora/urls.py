from django.urls import path

from my_apps.mora import views

app_name = "mora"

urlpatterns = [
    path("", views.MoraView.as_view(), name="home"),
]
