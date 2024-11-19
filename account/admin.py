from django.contrib import admin
from .models import Etudiant,Teacher
from django.contrib.auth.models import User
from unfold.admin import ModelAdmin
from django.utils.html import format_html
# Register your models here.
@admin.register(Etudiant)
class EtudiantAdmin(ModelAdmin):
    list_display = ['user_username','user_first_name','user_last_name', 'user_email', 'adresse', 'photo_thumbnail',]
    def user_username(self, obj):
        return obj.user.username  # Affiche le nom d'utilisateur du modèle User
    
    def user_first_name(self,obj):
        return obj.user.first_name
    
    def user_last_name(self,obj):
        return obj.user.last_name

    def user_email(self, obj):
        return obj.user.email  # Affiche l'email du modèle User

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)
        return '-'
    
    user_username.short_description = 'Nom d\'utilisateur'
    user_email.short_description = 'Email'
    user_last_name.short_description = "Nom"
    user_first_name.short_description = "Prenoms"
    photo_thumbnail.short_description = 'Photo'
    
@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = ['user_username','user_first_name','user_last_name', 'user_email', 'adresse', 'photo_thumbnail',]
    
    def user_username(self, obj):
        return obj.user.username  # Affiche le nom d'utilisateur du modèle User
    
    def user_first_name(self,obj):
        return obj.user.first_name
    
    def user_last_name(self,obj):
        return obj.user.last_name

    def user_email(self, obj):
        return obj.user.email  # Affiche l'email du modèle User

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)
        return '-'
    
    user_username.short_description = 'Nom d\'utilisateur'
    user_email.short_description = 'Email'
    user_last_name.short_description = "Nom"
    user_first_name.short_description = "Prenoms"
    photo_thumbnail.short_description = 'Photo'
    

admin.site.unregister(User)


# Filtre personnalisé
class UserTypeListFilter(admin.SimpleListFilter, ModelAdmin):
    title = 'Type d\'utilisateur'  # Titre du filtre
    parameter_name = 'user_type'

    def lookups(self, request, model_admin):
        return (
            ('teacher', 'Teacher'),
            ('etudiant', 'Etudiant'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'teacher':
            return queryset.filter(professeur__isnull=False)
        elif self.value() == 'etudiant':
            return queryset.filter(etudiant__isnull=False)
        return queryset

# Désenregistrement du modèle User existant dans l'admin

# Réenregistrement du modèle User avec le filtre personnalisé
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_filter = [UserTypeListFilter, 'is_active','is_superuser']
    list_display = ['username','first_name','last_name','etudiant__group']