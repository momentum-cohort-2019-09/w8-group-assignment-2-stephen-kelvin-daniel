# from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Flash.models import User, Deck, Card

@login_required
def dashboard(request):
    return render(request, "Flash/dashboard.html")

# Create your views here.
def test_deck(request, pk):
    return render(request, 'Flash/test_deck.html')

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

