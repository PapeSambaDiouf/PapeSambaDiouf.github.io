from django.shortcuts import render, redirect
from django.http import HttpResponse

import produit
from client.models import Client
from commande.forms import CommandeForm
from .models import Commande


# Create your views here.
def liste_commande(request):
    produits = produit.objects.all()
    clients = Client.objects.all()
    context = {'produits': produits, 'clients': clients}
    return render(request,"commande/liste_commande.html", context)


def ajoutercommande(request):


    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('/')
    context = {'form': form}
    return render(request,"commande/ajoutercommande.html",context)


def modifiercommande(request, pk):
    commande = Commande.objects.get(id=pk)

    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form = form.save()
            return redirect('/')
    context = {'form': form}
    return render(request,"commande/ajoutercommande.html",context)


def supprimercommande(request, pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')

    context = {'item': commande}

    return render(request,"commande/supprimercommande.html",context)

