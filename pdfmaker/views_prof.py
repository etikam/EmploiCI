from collections import defaultdict
from django.shortcuts import render, redirect
from EmploiApp.models import Licence, Group, Seance, Department, Semestre
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from xhtml2pdf import pisa

JOURS_SEMAINE = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']

@login_required(login_url='account:app_login')
def render_pdf_view_prof(request):
    if request.user.professeur:
        prof = request.user.professeur
        seances = Seance.objects.filter(professeur=prof).select_related('course', 'classroom', 'profDispoWeek')

        # Grouper les séances par jour
        seances_par_jour = defaultdict(list)
        for seance in seances:
            seances_par_jour[seance.get_day_week_display()].append(seance)

        # S'assurer que chaque jour est présent même s'il n'a pas de séance
        seances_avec_jours_vide = {day: seances_par_jour.get(day, []) for day in JOURS_SEMAINE}

        # URL absolue de l'image pour le PDF
        image_url = request.build_absolute_uri(static('assets/media/small_logo.png'))

        # Contexte avec les jours et séances
        context = {
            'seances_par_jour': seances_avec_jours_vide,
            'image_url': image_url,  # Inclure l'URL de l'image
        }
        
        template_path = 'pdfmaker/pdf_content.html'
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="Emploi_report.pdf"'

        # Rendu du template
        template = get_template(template_path)
        html = template.render(context)

        # Générer le PDF
        pdf = pisa.pisaDocument(html, dest=response)
        if pdf.err:
            return HttpResponse('Erreur lors de la génération du PDF.')
        
        return response
    else:
        return HttpResponse("Vous n'êtes pas un professeur")

