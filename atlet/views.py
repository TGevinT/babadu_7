from django.shortcuts import render, redirect
from django.db import connection
from atlet.models import Atlet

def enrolled_event(request):
    return render(request, 'enrolled_event.html')

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

def daftar_sponsor(request):
    return render(request, 'daftar_sponsor.html')

def daftar_event(request):
    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT nama, alamat, kapasitas, negara
        FROM STADIUM
    ''')
    stadium = cursor.fetchall()
    # print(stadium)
    # response.write(stadium_list)
    connection.close()

    stadium_list = []
    for item in stadium:
        stadium_list.append({
            'nama': item[0],
            'alamat': item[1],
            'kapasitas': item[2],
            'negara': item[3],
        })

    # print(stadium_list)

    context = {'stadium_list': stadium_list}
    # print(context)
    return render(request, "daftar_event.html", context)

def daftar_event_lanjut(request):

    if request.method == 'POST':
        stadium_pilih = request.POST.get('stadium')  # Get the selected stadium from the form

        cursor = connection.cursor()
        cursor.execute('''
            SELECT e.nama_event, e.total_hadiah, e.tgl_mulai, e.kategori_superseries
            FROM event e
            INNER JOIN stadium s ON s.nama = e.nama_stadium
            WHERE s.nama = %s
        ''', [stadium_pilih])
        events = cursor.fetchall()
        connection.close()

        event_list = []
        for event in events:
            event_list.append({
                'nama_event': event[0],
                'total_hadiah': event[1],
                'tgl_mulai': event[2],
                'kategori_superseries': event[3],
            })

        context = {
            'event_list': event_list,
            'stadium_pilih': stadium_pilih,
        }
        return render(request, 'daftar_event_lanjut.html', context)

    # If it's a GET request or no stadium selected yet, render the stadium selection page
    cursor = connection.cursor()
    cursor.execute('SELECT nama FROM stadium')
    stadiums = cursor.fetchall()
    connection.close()

    context = {'stadiums': stadiums}
    return render(request, 'daftar_event.html', context)

def daftar_partai(request):
    if request.method == 'POST':
        event_pilih = request.POST.get('event')  # Get the selected event from the form

        cursor = connection.cursor()
        cursor.execute('''
            SELECT pk.jenis_partai, pk.nama_event, pk.tahun_event,
                    e.nama_event, e.total_hadiah, e.tgl_mulai, e.tgl_selesai, e.kategori_superseries, 
                    s.nama as nama_stadium, s.kapasitas, s.negara
            FROM partai_kompetisi pk
            INNER JOIN event e ON e.nama_event = pk.nama_event 
            INNER JOIN stadium s ON s.nama = e.nama_stadium
            WHERE e.nama_event = %s
        ''', [event_pilih])
        partai_list = cursor.fetchall()
        connection.close()

        partai_kompetisi_list = []
        for partai in partai_list:
            partai_kompetisi_list.append({
                'jenis_partai': partai[0],
                'nama_event': partai[1],
                'tahun_event': partai[2],
                'nama_event': partai[3],
                'total_hadiah': partai[4],
                'tgl_mulai': partai[5],
                'tgl_selesai': partai[6],
                'kategori_superseries': partai[7],
                'nama_stadium': partai[8],
                'kapasitas': partai[9],
                'negara': partai[10],
            })

        context = {
            'partai_kompetisi_list': partai_kompetisi_list,
            'event_pilih': event_pilih,
        }
        return render(request, 'pilih_kategori.html', context)

    # If it's a GET request or no event selected yet, render the event selection page
    cursor = connection.cursor()
    cursor.execute('SELECT nama_event FROM event')
    events = cursor.fetchall()
    connection.close()

    context = {'events': events}
    return render(request, 'daftar_event_lanjut.html', context)


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


