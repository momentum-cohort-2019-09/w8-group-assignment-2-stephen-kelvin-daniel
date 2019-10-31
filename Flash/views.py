# from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Flash.models import User, Deck, Card

@login_required
def dashboard(request):
    all_decks = Deck.objects.all()
    return render(request, "Flash/dashboard.html", {
        "decks": all_decks,
    })

# Create your views here.
def testing(request):
    return render(request, 'Flash/testing.html')

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

