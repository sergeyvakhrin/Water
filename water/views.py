from django.shortcuts import render

def home(request):
    """ Контроллер стартовой страницы """
    context = {}
    return render(request, 'water/home.html', context)
