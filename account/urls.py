from django.urls import path 

from . import views

urlpatterns = [
    path('dashboard', views.dashboard_paj, name="dash"),
    path('enskripsyon', views.enskripsyon, name="signup"),
    path("konekte", views.koneksyon_user, name="connexion"),
    path('dekonekte', views.dekonekte_user, name="logout"),
]