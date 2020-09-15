from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="main"),
    path('exchange/', ExchangeCreateView.as_view()),
    path('test/', posterview)
	]