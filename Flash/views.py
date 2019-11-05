from django.forms import ModelForm, inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Flash.models import User, Deck, Card
from Flash.forms import DeckForm

#======================| Login for Collection of Cards/Deck/Info |===============================================#
@login_required
def dashboard(request):
    return render(request, "Flash/dashboard.html")

#======================| Test Deck Page |===============================================#
def test_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    card_list = deck.cards.all()
    card_obj = card_list.first()
    if request.method == 'GET' and 'card' in request.GET:
        card_obj = get_object_or_404(Card, pk=request.GET['card'])
    return render(request, 'Flash/test_deck.html', {'deck': deck, 'card_obj': card_obj})


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        exclude = [
            'user',
            'created_at',
            'updated_at',
            'is_active',
        ]

#======================| Edit Deck Page |===============================================#
def edit_deck(request, pk):
    deck = Deck.objects.get(pk=pk)
    DeckFormSet = inlineformset_factory(
        Deck,
        Card,
        fields=[
            'question',
            'answer',
        ])
    if request.method == "POST":
        card_formset = DeckFormSet(request.POST, request.FILES, instance=deck)
        deck_form = DeckForm(request.POST, request.FILES, instance=deck)
        if card_formset.is_valid() and deck_form.is_valid():
            card_formset.save()
            deck_form.save()
            return redirect(to='dashboard')
    else:
        card_formset = DeckFormSet(instance=deck)
        deck_form = DeckForm(instance=deck)
    return render(request, 'Flash/edit_deck_form.html', {
        'deck': deck,
        'deck_form': deck_form,
        'card_formset': card_formset
    })

#======================| Initial Page |===============================================#
def index_view(request):
    return render(request, "Flash/index.html")

#======================| Dashboard Page |===============================================#
@csrf_exempt
def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == "POST":
        deck.delete()
        return redirect(to='dashboard')
    return render(request, 'Flash/dashboard.html')

#======================| Add Deck Page |===============================================#
def add_deck(request, pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == "POST":
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = user
            deck.save()
            return redirect(to='dashboard')
    else:
        form = DeckForm()

    return render(request, "Flash/add_deck.html", {"form": form})
    
@csrf_exempt
def test_summary(request, pk):
    deck = get_error_or_404(Deck, pk=pk)
    card = get_error_or_404(Card, pk=pk)
    if request.method == "GET":
        return render(request, 'Flash/test_summary.html', 
            {'deck': deck, 'card_obj': card_obj, 'total_guesses': deck.total_guesses, 'total_correct_guesses': deck.total_correct_guesses})

@csrf_exempt
def correct_guess(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        card.total_guesses+=1
        card.total_correct_guesses+=1
        card.save()
        if(card.has_next_card):
            return render(request, "Flash/test_deck.html",{"deck":card.deck, 'card_obj': card.get_next_card()})
        else:
            print("end screen")

@csrf_exempt
def total_guesses(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        card.total_guesses+=1
        card.save()
        if(card.has_next_card):
            return render(request, "Flash/test_deck.html",{"deck":card.deck, 'card_obj': card.get_next_card()})
        else:
            print("end screen")
   
