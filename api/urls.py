from django.urls import path

from .views import *

urlpatterns = [
    path('', routesView, name='routes')
]
