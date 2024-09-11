from django import forms
from django.contrib.auth.models import User
from .models import Etudiant,Teacher

# Formulaire de traitement de la Classe Etudiant
class EtudiantForm(forms.ModelForm):
    
    class Meta:
        model = Etudiant
        fields = '__all__'
        
        
# Formulaire de traitement du model Teacher
class TeacherForm(forms.ModelForm):
    
    class Meta:
        model = Teacher
        fields = '__all__'
        

