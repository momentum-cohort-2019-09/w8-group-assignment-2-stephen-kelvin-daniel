# from django.shortcuts import render
from django.forms import ModelForm, inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
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
class DeckForm(ModelForm):
    class Meta:
        model = Deck
        exclude = [
            'user',
            'created_at',
            'updated_at',
        ]


def edit_deck(request,pk):
    deck = Deck.objects.get(pk=pk)
    DeckFormSet = inlineformset_factory(
        Deck, 
        Card, 
        fields=[
            'question',
            'answer',
        ])
    # form = DeckFormSet(request.POST, request.FILES, instance=deck)
    # if form.is_valid():
    #     form.save()
    #     return redirect(to='dashboard')
    if request.method == "POST":
        card_formset = DeckFormSet(request.POST, request.FILES, instance=deck)
        deck_form = DeckForm(reqeust.POST,request.FILES,instance=deck)
        if card_formset.is_valid() and deck_form.is_valid():
            card_formset.save()
            deck_form.save()
            return redirect(to='dashboard')
    else:
        card_formset = DeckFormSet(instance=deck)
        deck_form = DeckForm(instance=deck)
    return render(request, 'Flash/edit_deck_form.html',{
        'deck_form':deck_form,
        'card_formset':card_formset
        })    


def index_view(request):
    return render(request, "Flash/index.html")

@csrf_exempt
def delete_deck(request,pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == "POST":
        deck.delete()
        return redirect(to='dashboard')
    return render(request, 'Flash/dashboard.html')

# class AddDeckView(CreateView):
#     model = Deck
#     self.object.user =
#     template_name = "Flash/add_deck.html"
#     fields = ['subject','title','description']
