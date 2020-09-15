from django.shortcuts import render

# Create your views here.

def matches(request):
    """ A view to go to team.html """

    return render(request, 'matches/matches.html')