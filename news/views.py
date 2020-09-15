from django.shortcuts import render

# Create your views here.

def news(request):
    """ A view to go to team.html """

    return render(request, 'news/news.html')