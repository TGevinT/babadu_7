from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Atlet


def daftar_atlet(request):

    if request.method == 'POST':
        atlet_terdaftar = request.POST['atlet']
        atlet = Atlet(nama=atlet_terdaftar)
        atlet.save()
        create_dummy_data()
        return redirect('list_atlet')

    atlet_list = ['Atlet 1', 'Atlet 2', 'Atlet 3']
    return render(request, 'daftar_atlet.html', {'atlet_list': atlet_list})

def index(request):
    return render(request, 'index.html')

def form_kualifikasi(request):
    if request.method == 'POST':
        # proses validasi form
        # jika form valid, redirect ke halaman pertanyaan_kualifikasi
        return redirect('pertanyaan_kualifikasi/')
    else:
        return render(request, 'form_kualifikasi.html')

def pertanyaan_kualifikasi(request):
    return render(request, 'pertanyaan_kualifikasi.html')


def list_atlet(request):
    atlet_list = Atlet.objects.all()
    return render(request, 'list_atlet.html', {'atlet': atlet_list})

def create_dummy_data():
    atlet1 = Atlet(nama='Atlet 1', email='atlet1@example.com', world_rank=10)
    atlet1.save()
    atlet2 = Atlet(nama='Atlet 2', email='atlet2@example.com', world_rank=20)
    atlet2.save()
    atlet3 = Atlet(nama='Atlet 3', email='atlet3@example.com', world_rank=30)
    atlet3.save()

def dash_atlet(request):
    return render(request, 'atlet.html')
