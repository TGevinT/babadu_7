from django.shortcuts import render
from django.db import connection
from django import template
from umpire.models import Atlet_kualifikasi, Member, Atlet, Point_history, Atlet_non_kualifikasi, Atlet_ganda, Partai_kompetisi, Event, Stadium
from django.shortcuts import render
from django.db import connection

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



def show_daftar_atlet(request):
    cursor = connection.cursor()

    # Fetch data for Atlet Kualifikasi
    query = """
    SELECT atlet_kualifikasi.id_atlet, member.nama, atlet.tgl_lahir, atlet.negara_asal, atlet.play_right,
           atlet.height, atlet_kualifikasi.world_rank, atlet.jenis_kelamin, SUM(point_history.total_point) AS total_point
    FROM atlet_kualifikasi
    INNER JOIN member ON atlet_kualifikasi.id_atlet = member.id
    INNER JOIN atlet ON atlet_kualifikasi.id_atlet = atlet.id
    LEFT JOIN point_history ON point_history.id_atlet = atlet_kualifikasi.id_atlet
    GROUP BY atlet_kualifikasi.id_atlet, member.nama, atlet.tgl_lahir, atlet.negara_asal, atlet.play_right,
             atlet.height, atlet_kualifikasi.world_rank, atlet.jenis_kelamin
    """
    cursor.execute(query)
    atlet_kualifikasi_data = cursor.fetchall()

    # Fetch data for Atlet Non-Kualifikasi
    query = """
    SELECT atlet_non_kualifikasi.id_atlet, member.nama, atlet.tgl_lahir, atlet.negara_asal, atlet.play_right,
           atlet.height, atlet.world_rank, atlet.jenis_kelamin, SUM(point_history.total_point) AS total_point
    FROM atlet_non_kualifikasi
    INNER JOIN member ON atlet_non_kualifikasi.id_atlet = member.id
    INNER JOIN atlet ON atlet_non_kualifikasi.id_atlet = atlet.id
    LEFT JOIN point_history ON point_history.id_atlet = atlet_non_kualifikasi.id_atlet
    GROUP BY atlet_non_kualifikasi.id_atlet, member.nama, atlet.tgl_lahir, atlet.negara_asal, atlet.play_right,
             atlet.height, atlet.world_rank, atlet.jenis_kelamin
    """
    cursor.execute(query)
    atlet_non_kualifikasi_data = cursor.fetchall()

    # Fetch data for Atlet Ganda
    query = """
    SELECT atlet_ganda.id_atlet_ganda, member1.nama AS nama_atlet_1, member2.nama AS nama_atlet_2, 
           SUM(point_history.total_point) AS total_point
    FROM atlet_ganda
    INNER JOIN member AS member1 ON atlet_ganda.id_atlet_kualifikasi = member1.id
    INNER JOIN member AS member2 ON atlet_ganda.id_atlet_kualifikasi_2 = member2.id
    LEFT JOIN point_history ON point_history.id_atlet = atlet_ganda.id_atlet_kualifikasi
                             OR point_history.id_atlet = atlet_ganda.id_atlet_kualifikasi_2
    GROUP BY atlet_ganda.id_atlet_ganda, member1.nama, member2.nama
    """
    cursor.execute(query)
    atlet_ganda_data = cursor.fetchall()

    return render(request, 'daftarAtlet.html', {
        "data1": atlet_kualifikasi_data,
        "data2": atlet_non_kualifikasi_data,
        "data3": atlet_ganda_data,
    })



def show_event(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT pk.jenis_partai, e.nama_event, e.tahun, e.nama_stadium, e.kategori_superseries, e.tgl_mulai, e.tgl_selesai, s.kapasitas
            FROM partai_kompetisi AS pk
            JOIN event AS e ON pk.nama_event = e.nama_event
            JOIN stadium AS s ON e.nama_stadium = s.nama
            '''
        )
        rows = cursor.fetchall()

    events = []
    for row in rows:
        event = {
            'jenis_partai': row[0],
            'nama_event': row[1],
            'tahun': row[2],
            'nama_stadium': row[3],
            'kategori_superseries': row[4],
            'tgl_mulai': row[5],
            'tgl_selesai': row[6],
            'kapasitas': row[7],
        }
        events.append(event)

    return render(request, 'event.html', {'events': events})


