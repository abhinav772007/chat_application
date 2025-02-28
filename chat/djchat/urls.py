from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.house, name='house'),
    path('signup/', views.signup, name='signup'),
    path('<str:room_name>/', views.rom, name='rom'),
    path('checkview', views.checkview, name='checkview'), 
    path('send', views.send, name='send'),
    path('getMessages/<str:room_name>/', views.get_messages, name='getMessages') , 
    path('signin/', views.signin, name='signin'),
    path('Feeedback/', views.Feedback, name='Feedback'),
]
