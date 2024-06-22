# salary_dashboard/urls.py
from django.contrib import admin
from django.urls import path, re_path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("stats/", views.stats, name="stats"),
]
