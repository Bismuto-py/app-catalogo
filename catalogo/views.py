from django.shortcuts import render, get_object_or_404
from .models import Obra

def index(request):
    obras = Obra.objects.all()
<<<<<<< HEAD
=======
    context = {
        "obras": obras,
    }

    return render(
        request,
        "catalogo/index.html",
        context
    )
>>>>>>> 5fa293f847a9d5e0eca6388be6f2c87217fe4d7a

    return render(request, "catalogo/index.html", {
        "obras": obras
    })

def detalhes(request, id):
    obra = get_object_or_404(Obra, id=id)

<<<<<<< HEAD
    return render(request, "catalogo/detalhes.html", {
        "obra": obra
    })
=======
    obra = get_object_or_404(Obra, id=id)

    context = {
        "obra": obra,
    }

    return render(
        request,
        "catalogo/detalhes.html",
        context
    )
>>>>>>> 5fa293f847a9d5e0eca6388be6f2c87217fe4d7a
