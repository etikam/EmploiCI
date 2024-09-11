from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

# Class Utilisateur Etudiant  personnalisé


class Etudiant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('EmploiApp.Group', on_delete=models.CASCADE)
    semestre = models.ForeignKey('EmploiApp.Semestre', on_delete=models.CASCADE)
    def __str__(self):
        return self.username

    class Meta:
        verbose_name= 'Etudiant'
        

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=100)
    def __str__(self): 
        return self.username
    
    class Meta:
        verbose_name= 'Teacher'