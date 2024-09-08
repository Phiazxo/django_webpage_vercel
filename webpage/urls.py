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
    path("detall/", views.detallPage, name="detall"),
    path("buttons/", views.buttonsPage, name="buttons"),
    path("cards/", views.cardsPage, name="cards"),
    path("colors/", views.colorsPage, name="colors"),
    path("borders/", views.bordersPage, name="borders"),
    path("animations/", views.animationsPage, name="animations"),
    path("other/", views.otherPage, name="other"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("forgot_password/", views.forgot_passwordPage, name="forgot_password"),
    path("404_page/", views.errorPage, name="404_page"),
    path("blank_page/", views.blankPage, name="blank_page"),
    path("charts/", views.chartsPage, name="charts"),
    path("tables/", views.tablesPage, name="tables"),
]