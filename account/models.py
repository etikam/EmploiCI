from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User

# User = get_user_model()
# Create your models here.

# Class Utilisateur Etudiant  personnalisé



class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="etudiant")
    group = models.ForeignKey('EmploiApp.Group', on_delete=models.CASCADE)
    telephone = models.CharField(max_length = 20,blank=True, null=True )

    photo = models.ImageField(upload_to='student_profils', null=True, blank=True)
    adresse = models.CharField(max_length=100,blank=True, null=True)
    def __str__(self):
        return f'{self.user.username}-{self.user.first_name}-{self.user.last_name}'

    class Meta:
        verbose_name= 'Etudiant'

    def delete(self, *args, **kwargs):
        """Supprimer l'utilisateur associé avant de supprimer l'Etudiant."""
        # Supprimer l'utilisateur associé
        print("=============la suppression commmence ===========")
        if self.user:
            self.user.delete()
        # Supprimer l'instance Etudiant
        super(Etudiant, self).delete(*args, **kwargs)


        
# Model professeur personnalisé
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="professeur")
    # telephone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)  # Ajout du champ photo de profil
    adresse = models.CharField(max_length=255, blank=True, null=True)  # Ajout du champ adresse
    cv = models.FileField(upload_to='teacher_cvs/', blank=True, null=True)  # Ajout du champ CV
    bio = models.TextField(max_length=500)
    
    def __str__(self): 
        return f'{self.user.first_name} {self.user.last_name}'
    
    class Meta:
        verbose_name= 'Professeur'
        
    def delete(self, *args, **kwargs):
        """Supprimer l'utilisateur associé avant de supprimer le Teacher."""
        # Supprimer l'utilisateur associé
        if self.user:
            self.user.delete()
        # Supprimer l'instance Teacher
        super(Teacher, self).delete(*args, **kwargs)



