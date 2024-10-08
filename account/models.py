from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

User = get_user_model()
# Create your models here.

# Class Utilisateur Etudiant  personnalisé

class Etudiant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('EmploiApp.Group', on_delete=models.CASCADE)
    pv = models.CharField(max_length = 150)
  
    def __str__(self):
        return f'{self.user.username}-{self.user.first_name}-{self.user.last_name}'

    class Meta:
        verbose_name= 'Etudiant'

        
# Model professeur personnalisé
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)  # Ajout du champ photo de profil
    adresse = models.CharField(max_length=255, blank=True, null=True)  # Ajout du champ adresse
    cv = models.FileField(upload_to='teacher_cvs/', blank=True, null=True)  # Ajout du champ CV
    
    def __str__(self): 
        details = (f'{self.user.username} - {self.user.first_name} - {self.user.last_name} - '
                f'Téléphone: {self.telephone} - Adresse: {self.adresse}')
        
        if self.photo:
            details += f' - Photo: {self.photo.url}'
        if self.cv:
            details += f' - CV: {self.cv.url}'
        
        return details


    class Meta:
        verbose_name = 'Teacher'


