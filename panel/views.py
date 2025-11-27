from django.shortcuts import render
from .models import Emprendimiento

def lista_emprendimientos(request):
    emprendimientos = Emprendimiento.objects.all()
    return render(request, 'panel/emprendimientos.html', {'emprendimientos': emprendimientos})
