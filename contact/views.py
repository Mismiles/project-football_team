from django.shortcuts import render

# Create your views here.

def contact(request):
    """ A view to go to contact.html """

    return render(request, 'contact/contact.html')