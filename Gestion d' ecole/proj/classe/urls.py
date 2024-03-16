
from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.liste_classe,name='classe'),
    path('delete/<int:id>/',views.delete_classe, name="deletedatac"),
    path('<int:id>/',views.update_classe, name="updatedata"),
]
