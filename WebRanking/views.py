from .models import Player,Match
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import NameForm
from .source import ranking

def homepage(request):
    all_players = Player.objects.all().order_by("-ranking")

    return render(request, 'rankings/homepage.html', {'players': all_players})

def index(request):
    #Using the paginator to display fewer results per page
    all_players = Player.objects.all().order_by("-ranking")
    page = request.GET.get('page', 1)
    paginator = Paginator(all_players, 30)

    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(paginator.num_pages)

    return render(request, 'rankings/index.html', {'players': players})

def matches(request):
    all_matches = Match.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_matches, 30)

    try:
        matches = paginator.page(page)
    except PageNotAnInteger:
        matches = paginator.page(1)
    except EmptyPage:
        matches = paginator.page(paginator.num_pages)

    return render(request, 'rankings/matches.html', {'matches': matches})

def addmatch(request):
    all_players = Player.objects.all().order_by("-ranking")
    if request.method == 'POST':  # If the form has been submitted...
        form = NameForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            first_player = Player.objects.get(pk=int(form['first_player'].value()))
            second_player = Player.objects.get(pk=int(form['second_player'].value()))
            if (first_player==second_player):
                messages.error(request, 'Choose different players!')
                return render(request, 'rankings/homepage.html', {'players': all_players})
            first_per = float(request.POST['first_per'])
            second_per = float(request.POST['second_per'])
            performances = ((first_player.name,first_per),(second_player.name,second_per))
            rankings = {first_player.name:first_player.ranking,second_player.name:second_player.ranking}
            updated_rankings = ranking.apply_multiplayer_updates(performances,rankings)
            if (updated_rankings[first_player.name] > first_player.ranking): #If the first player has higher ranking after the match he is the winner
                match = Match(winner=first_player.name)
                messages.success(request, 'Rankings updated!')
            elif (updated_rankings[first_player.name] == first_player.ranking): #Just in case for future development
                match = Match(winner="Draw")
            else:
                match = Match(winner=second_player.name)
                messages.success(request, 'Rankings updated')
            match.save()
            match.players.add(first_player,second_player)
            #Updating the rankings of the player in the database with the updated rankings
            first_player.ranking = updated_rankings[first_player.name]
            second_player.ranking = updated_rankings[second_player.name]
            first_player.performances += 1
            second_player.performances += 1
            first_player.save()
            second_player.save()
            return render(request, 'rankings/homepage.html', {'players': all_players})
    else:
        form = NameForm()  # An unbound form

    return render(request, 'rankings/homepage.html', {'players': all_players})

def aboutme(request):
    return render(request, 'rankings/aboutme.html')
