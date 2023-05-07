from django.shortcuts import render


def dash_umpire(request):
    return render(request, 'umpire.html')

def show_pertandingan(request):
    return render(request, 'pertandingan.html')