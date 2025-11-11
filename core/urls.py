from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('find-facility/', views.find_facility, name='find_facility'),
    path('awareness/', views.awareness, name='awareness'),
    path("locator/", views.locator, name="locator"),
    path("locations/<int:id>/", views.locator_detail, name="locator_detail"),
    path('api/locations/', views.api_locations, name='api_locations'),
]
