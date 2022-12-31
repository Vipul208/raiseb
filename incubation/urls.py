from django.urls import path

from . import views

app_name = "incubation"
urlpatterns = [
    path("", views.home, name="home"),
    path('contacts', views.contacts, name='contacts'),
    path("<int:pk>-<str:slug>/", views.detail_view, name="detail"),

]
