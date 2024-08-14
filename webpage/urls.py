from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutPage, name="about"),
    path("contact/", views.contactPage, name='contact'),
    path("for/", views.forPage, name='for'),
    path("card/", views.cardPage, name='card'),
    path("card_color/", views.cardcolorPage, name='card_color'),
    path("form/", views.formPage, name='form'),
]