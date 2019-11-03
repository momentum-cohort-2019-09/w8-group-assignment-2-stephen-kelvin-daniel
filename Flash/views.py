# from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Flash.models import User, Deck, Card

@login_required
def dashboard(request):
    return render(request, "Flash/dashboard.html")

# def test_deck(request, pk):
#     deck = get_object_or_404(Deck, pk=pk)
#     return render(request, 'Flash/test_deck.html', {"deck": deck})

def test_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    card_list = deck.cards.all()
    card_obj = card_list.first()
    if request.method == 'GET' and 'card' in request.GET:
        card_obj = get_object_or_404(Card, pk=request.GET['card'])
    return render(request, 'Flash/test_deck.html', {'deck': deck, 'card_obj': card_obj})

# def viewDeck(request, deck_id):
#     deck_obj = get_object_or_404(Deck, id=deck_id)
#     card_list = deck_obj.card_set.all()
#     card_obj = card_list.first()
#     if request.method == 'GET' and 'card' in request.GET:
#         card_obj = get_object_or_404(Card, id=request.GET['card'])
#     context = {'deck_obj': deck_obj, 'card_obj':card_obj}
#     return render(request, 'flashcards/viewDeck.html', context)

# def dashboard(request):
#     return render(request, 'Flash/dashboard.html')


def edit_deck(request):
    return render(request, 'Flash/edit_deck.html')    

# @ login_required
# def index_views(request):

def index_view(request):
    return render(request, "Flash/index.html")
# def accounts_login(request):

#     user = request.user
#     return render(request, "Flash/index.html", {"user": user})

