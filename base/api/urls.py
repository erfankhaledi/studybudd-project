
from xml.etree.ElementInclude import include
from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
    
]