from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_page, name='properties'),
    path('<int:property_id>', views.property, name='property'),
    path('search', views.search, name='search'),

]
