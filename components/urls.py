from django.contrib import admin
from django.urls import path, include

from components.views import components_view

urlpatterns = [
    path('admin/components/', components_view, name='components_view'),
]