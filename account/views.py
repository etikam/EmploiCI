from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages

def account_activation_view(request):
    if request.method == 'POST':
        step = request.POST.get('step')
        
        # Step 1: Matricule et Département
        if step == '1':
            matricule = request.POST.get('matricule')
            departement = request.POST.get('departement')
            if not matricule or not departement:
                messages.error(request, "Tous les champs sont requis pour cette étape.")
                return render(request, 'account/register.html', {'step': '1'})
            
            # Stocker les données dans la session
            request.session['matricule'] = matricule
            request.session['departement'] = departement

            return redirect(reverse('account_activation_step2'))
        
        # Step 2: Mot de passe
        elif step == '2':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm-password')
            if password != confirm_password:
                messages.error(request, "Les mots de passe ne correspondent pas.")
                return render(request, 'account/register.html', {'step': '2'})
            
            # Stocker le mot de passe dans la session
            request.session['password'] = password

            # Rediriger vers la page de succès
            return redirect(reverse('account_activation_success'))
    
    # Par défaut, afficher la première étape
    return render(request, 'account/register.html', {'step': '1'})


def account_activation_step2(request):
    return render(request, 'account/register.html', {'step': '2'})


def account_activation_success(request):
    # Ici, vous pouvez traiter les données enregistrées dans la session (e.g., sauvegarder dans la base de données)
    matricule = request.session.get('matricule')
    departement = request.session.get('departement')
    password = request.session.get('password')

    # Faire ce qu'il faut avec ces données (enregistrer un utilisateur, envoyer un email, etc.)
    
    return HttpResponse("Votre compte a été activé avec succès.")
