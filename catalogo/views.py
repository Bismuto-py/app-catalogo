from django.shortcuts import render, get_object_or_404
from .models import Obra

def index(request):
    obras = Obra.objects.all()

    return render(request, "catalogo/index.html", {
        "obras": obras
    })

def detalhes(request, id):
    obra = get_object_or_404(Obra, id=id)

    return render(request, "catalogo/detalhes.html", {
        "obra": obra
    })