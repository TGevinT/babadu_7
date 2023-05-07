from django.shortcuts import render


def dash_atlet(request):
    return render(request, 'atlet.html')
