from django.db import models 

# Create your models here.
class etud(models.Model):
    
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70)
    N_Tel = models.CharField(max_length=30)
    classe = models.CharField(max_length=30)
  
   
   