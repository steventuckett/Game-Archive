from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from .models import Console, Game

def index(request):
    return render(request, 'core/index.html')

def console(request):
    latest_console_list = Console.objects.order_by('-name')[:10]
    context = {'latest_console_list': latest_console_list,}
    return render(request, 'core/console.html', context)

def game(request, console_id):
    console = Console.objects.get(pk=console_id)
    return render(request, 'core/game.html', {'console': console})

def detail(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'core/details.html', {'game': game})

