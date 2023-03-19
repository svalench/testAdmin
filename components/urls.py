from django.contrib import admin
from django.urls import path, include

from components.views import components_view, save_component_status

urlpatterns = [
    path('admin/components/', components_view, name='components_view'),
    path('admin/components/save_component_status', save_component_status, name='save_component_status'),
]