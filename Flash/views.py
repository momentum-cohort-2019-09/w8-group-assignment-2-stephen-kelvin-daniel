# from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Flash.models import User, Deck, Card
def dashboard(request):
    all_decks = Deck.objects.all()
    return render(request, "Flash/dashboard.html", {
        "decks": all_decks,
    })

# Create your views here.
def testing(request):
    return render(request, 'Flash/testing.html')

# @login_required
# def dashboard(request):
#     return render(request, 'Flash/dashboard.html')

def index_view(request):
    return render(request, "Flash/index.html")
# def accounts_login(request):
#     user = request.user
#     return render(request, "Flash/index.html", {"user": user})

