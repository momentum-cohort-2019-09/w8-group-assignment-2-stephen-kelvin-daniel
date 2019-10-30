from django.shortcuts import render, redirect, get_object_or_404
from Flash.models import Card, Deck


def deck_list(request):
    all_decks = Deck.objects.all()
    return render(request, "Flash/dashboard.html", {
        "decks": all_decks,
    })
