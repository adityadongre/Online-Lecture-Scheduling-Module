from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_panel, name='home_panel'),
    path('admin/', views.admin_panel, name='admin_panel'),
    path('instructor/', views.instructor_panel, name='instructor_panel'),
]
