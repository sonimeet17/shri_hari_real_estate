from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_page, name='display_page'),
    path('about', views.about, name='about'),
]
