from collections import defaultdict
from django.shortcuts import render,redirect
from EmploiApp.models import Licence, Group, Seance, Department, Semestre
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from xhtml2pdf import pisa
# Create your views here.
@login_required(login_url='account:app_login')
def emploi(request):
    if not request.user.is_superuser:
        return redirect('emploi:app_home')
        # Récupération des départements, licences et semestres
    departments = Department.objects.all()
    groups = Group.objects.all().order_by('licence')
    semestres = Semestre.objects.all()

    # Passer les données au contexte pour les utiliser dans le template
    context = {
        'departments': departments,
        'groups': groups,
        'semestres': semestres
    }
    return render(request, 'pdfmaker/show.html', context)


# Liste des jours de la semaine en fonction de ton modèle
JOURS_SEMAINE = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']


@login_required(login_url='account:app_login')
def render_pdf_view(request):
    if not request.user.is_superuser:
        return redirect('emploi:app_home')
    if request.method == "POST":
        group_id = request.POST.get('group_id')
        try:
            group = Group.objects.select_related('licence', 'licence__department').get(id=group_id)
            seances = Seance.objects.filter(group=group).select_related('course', 'classroom', 'profDispoWeek')

            # Grouper les séances par jour
            seances_par_jour = defaultdict(list)
            for seance in seances:
                seances_par_jour[seance.get_day_week_display()].append(seance)

            # S'assurer que chaque jour est présent même s'il n'a pas de séance
            seances_avec_jours_vide = {day: seances_par_jour.get(day, []) for day in JOURS_SEMAINE}
            image_url = request.build_absolute_uri(static('assets/media/small_logo.png'))
            # Contexte avec le groupe et ses séances
            context = {
                'group': group,
                'seances_par_jour': seances_avec_jours_vide,
                'image_url': image_url,
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

        except Group.DoesNotExist:
            return HttpResponse('Groupe introuvable.', status=404)
    else:
        return redirect(emploi)
