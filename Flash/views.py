# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm, inlineformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Flash.models import User, Deck, Card

@login_required
def dashboard(request):
    return render(request, "Flash/dashboard.html")

# Create your views here.
def testing(request):
    return render(request, 'Flash/testing.html')

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
