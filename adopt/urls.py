from django.urls import path

from . import views

urlpatterns = [
   # path('/adopt/', views.
    path('list/', views.all_pets),
    path('<int:pet_id>/', views.pet_details),
    path('<int:pet_id>/edit/', views.edit_pet),
    path(add/', views.add_pet),
]
