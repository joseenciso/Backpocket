from django.shortcuts import render

# Create your views here.

def profile(request):
    """ User's profile """
    template = 'profiles/profiles.html'
    context = {}

    return render(request, template, context)