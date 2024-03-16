
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login,name='login'),
    path('accueil',views.list,name='list'),
    path('home',views.home,name='accueil'),
    path('<int:id>/',views.update_etudient, name="modifieretudient"),
    path('delete/<int:id>/',views.delete_etudient,name="suprimeretudient"),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),  
    
]
