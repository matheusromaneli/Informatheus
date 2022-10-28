from django.shortcuts import render
from cards.models import Card

# Create your views here.
def index(request):
    lista_cards = Card.objects.all()
    return render(request, 'cards/index.html', { "cards": lista_cards })