from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') #if first paramater blank = home url
]
