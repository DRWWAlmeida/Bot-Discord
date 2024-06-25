from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('api', views.api, name='api'),

]
