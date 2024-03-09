from django.shortcuts import render

# Create your views here.

def inscriptionPage(request):
    context = {}
    return render(request, 'compte/inscription.html', context)
