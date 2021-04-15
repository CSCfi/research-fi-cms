from django.urls import path
from . import views

urlpatterns = [
    path("db", views.backup_db, name="backup_db"),
    path("media", views.backup_media, name="backup_media"),
    path("all", views.backup_db_and_media, name="backup_db_and_media"),
]