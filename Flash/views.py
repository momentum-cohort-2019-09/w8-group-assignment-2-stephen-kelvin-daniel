# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
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


def edit_deck(request):
    return render(request, 'Flash/edit_deck.html')    

# @ login_required
# def index_views(request):

def index_view(request):
    return render(request, "Flash/index.html")

@csrf_exempt
def delete_deck(request,pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == "POST":
        deck.delete()
        return redirect(to='dashboard')
    return render(request, 'Flash/dashboard.html')

