from django.shortcuts import render

# Create your views here.

from .models import PokemonCard


def index(request):

    stuff = PokemonCard.objects.all()

    context = {
        "stuff": stuff
    }

    return render(request, "index.html", context)
