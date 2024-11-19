from django.contrib import admin

from EmploiApp.forms import SeanceForm
from .models import ( Department,
                    Group, Licence, Semestre,
                    ProfDispoWeek,
                    Course, Classroom,
                    Rapport,
                    Seance
                    )
from unfold.admin import ModelAdmin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
# Register your models here.



@admin.register(Department)
class DepartmentAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("label",)}
    
@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass


@admin.register(Semestre)
class SemestreAdmin(ModelAdmin):
    pass



@admin.register(ProfDispoWeek)
class ProfDispoWeekAdmin(ModelAdmin):
    list_display = ['teacher','day_week','busy', 'start_time', 'end_time']
    list_filter = ['teacher','day_week']
    pass
@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_filter = ['semestre']

@admin.register(Classroom)
class ClassroomAdmin(ModelAdmin):
    pass

@admin.register(Seance)
class SeanceAdmin(ModelAdmin):
    form = SeanceForm
    list_display = ['course', 'day_week', 'classroom', 'profDispoWeek']  # Ajout de day_week
    list_filter = ['course', 'classroom', 'profDispoWeek__day_week', 'profDispoWeek__teacher', 'day_week']  # Ajout de day_week
    
    class Media:
        js = ('assets/js/charge_dispo.js',)

    def save_model(self, request, obj, form, change):
        selected_groups = form.cleaned_data.get('group', [])

        errors = []
        for group in selected_groups:
            overlapping_group_seances = Seance.objects.filter(
                group=group,
                day_week=obj.day_week,
                h_start__lt=obj.h_end,
                h_end__gt=obj.h_start
            ).exclude(id=obj.id)

            if overlapping_group_seances.exists():
                # Ajouter l'erreur à la liste
                errors.append(
                    _('Le groupe %(group)s est déjà affecté à une autre séance durant cette période.') % {'group': group}
                )

        if errors:
            # Ajouter les erreurs au formulaire et les envoyer comme flash messages
            form.add_error('group', '\n'.join(errors))
            # Ajouter un message flash pour l'utilisateur
            messages.error(request, '\n'.join(errors))
        else:
            # Si pas d'erreurs, enregistrer l'objet normalement
            super().save_model(request, obj, form, change)
    
@admin.register(Licence)
class LicenceAdmin(ModelAdmin):
   pass
    # list_filter  = ['day_week','start_time','end_time']
    


from django.urls import reverse
from django.utils.html import format_html

class RapportAdmin(ModelAdmin):
    list_display = ('title', 'view_link')

    def view_link(self, obj):
        url = reverse('create_pdf')  # Remplacez 'create_pdf' par le nom de votre vue
        return format_html('<button><a href="{}" class="btn btn-primary">Imprimer</a></button>', url)

    view_link.short_description = 'Cliquer pour imprimer'

admin.site.register(Rapport, RapportAdmin)
