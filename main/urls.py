from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('home', views.homescreen, name='home'),
    path('creatingquestion', views.creatingquestion, name='creatingquestion'),
    path('generatingtests', views.generatingtests, name='generatingtests'),
    path('questionlibarary', views.questionlibarary, name='questionlibaray'),
    path('tagcreator', views.tagcreator, name='tagcreator'),
    path('testlibarary', views.testlibarary, name='testlibarary'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
]