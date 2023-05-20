from django.shortcuts import render


def show_pelatih(request):
    return render(request, 'pelatih.html')
