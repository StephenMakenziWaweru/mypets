from django.urls import path
from . import views

urlpatterns = [
    path('', views.PetsListView.as_view(), name='pets'),
    path('new/', views.PetsCreateView.as_view(), name='pets-create'),
]
