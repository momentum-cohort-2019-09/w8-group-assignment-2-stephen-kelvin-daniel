from django import forms
from Flash.models import Deck, Card

class DeckForm(forms.ModelForm):

    class Meta:
        model = Deck
        fields = ['subject', 'title','description']
