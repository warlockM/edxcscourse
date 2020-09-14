from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name = "contact" ),
    path("save", views.save_contact, name = "saved"),
    path("aboutus", views.aboutus, name = "aboutus"),
    path("infra", views.infra, name = "infra"),
    path("stateinfra/<str:name>", views.stateinfra, name = "stateinfra")
    #path("edu", views.edu, name = "edu"),
    #path("stateedu/<str:name>", views.edu, name = "stateedu"),
    #path("health", views.health, name = "health"),
    #path("statehealth/<str:name>", views.health, name = "statehealth")
]
