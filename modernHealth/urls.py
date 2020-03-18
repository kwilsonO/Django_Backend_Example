from django.urls import path
from rest_framework import routers
from modernHealth.programLibrary import views

router = routers.DefaultRouter()

urlpatterns = [
    path('modernHealth/programlibrary/get/<program_name>', views.getProgram),
    path('sample/endpoint', views.helloWorld)
]