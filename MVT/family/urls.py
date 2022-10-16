from django.urls import path

from family import views

app_name = "family"
urlpatterns = [
    path("relatives", views.relatives, name="relatives-list"),
]
