from django.shortcuts import render


def dash_umpire(request):
    return render(request, 'umpire.html')
