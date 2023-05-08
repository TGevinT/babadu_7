from django.shortcuts import render


def dash_umpire(request):
    return render(request, 'umpire.html')

def show_pertandingan(request):
    return render(request, 'pertandingan.html')

def show_semifinal(request):
    return render(request, 'semifinal.html')

def show_final(request):
    return render(request, 'final.html')

def show_hasil(request):
    return render(request, 'hasil.html')

def show_hasil_pertandingan(request):
    return render(request, 'hasil_pertandingan.html')