from django.shortcuts import render, redirect
from utils.query import query
import uuid

import logging

logger = logging.getLogger("debugger")

# DASHBOARD
def dashboard_atlet(request):
    if 'user_id' not in request.session: 
        logger.info('A')
        return redirect('/authentication/login')
    
    if request.session['user_role'] != 'ATLET':
        raise Exception

    user = f"""
        SELECT 
        M.nama, M.email, A.tgl_lahir, A.negara_asal, 
        A.play_right, A.height, A.world_rank, A.jenis_kelamin
        FROM MEMBER M, ATLET A
        WHERE M.id = A.id AND M.id = '{request.session.get('user_id')}'
    """
    atlet = query(user)
    if atlet:
        logger.info('B')
        context = {
            'nama': atlet[0].get('nama'),
            'email': atlet[0].get('email'),
            'tgl_lahir': atlet[0].get('tgl_lahir'),
            'negara': atlet[0].get('negara_asal'),
            'play': atlet[0].get('play_right'),
            'tinggi': atlet[0].get('height'),
            'world_rank': atlet[0].get('world_rank'),
            'jenis_kelamin': atlet[0].get('jenis_kelamin'),
            'world_rank': atlet[0].get('world_rank'),
            'status': get_status_atlet(request.session['user_id']),
            'pelatih': get_pelatih_atlet(request.session['user_id']),
            'total_point': get_total_point(request.session['user_id'])
        }
        return render(request, 'dashboard-atlet.html', context)


def dashboard_pelatih(request):
    if 'user_id' not in request.session: 
        logger.info('A')
        return redirect('/authentication/login')
    user = f"""
        SELECT m.nama, m.email, p.*
        FROM member m, pelatih p
        WHERE m.id = p.id
        AND m.id='{request.session.get('user_id')}'::uuid
        """
    pelatih = query(user)
    if pelatih:
        logger.info('B')
        context = {
            'id': pelatih[0]['id'],
            'nama': pelatih[0]['nama'],
            'spesialisasi': 'ini blm dihandle. bakal make string aggregate',
            'email': pelatih[0]['email'],
            'tanggal_mulai': pelatih[0]['tanggal_mulai']
        }
        return render(request, 'dashboard-pelatih.html', context)
    else:
        # unauthorized page view
        logger.info('C')
        raise Exception

def dashboard_umpire(request):
    if 'user_id' not in request.session: 
        logger.info('A')
        return redirect('/authentication/login')
    user = f"""
        SELECT m.nama, m.email, u.*
        FROM member m, umpire u
        WHERE m.id = u.id
        AND m.id='{request.session.get('user_id')}'::uuid
        """
    umpire = query(user)
    if umpire:
        logger.info('B')
        context = {
            'id': umpire[0]['id'],
            'nama': umpire[0]['nama'],
            'spesialisasi': 'ini blm dihandle. bakal make string aggregate',
            'email': umpire[0]['email'],
            'tanggal_mulai': umpire[0]['tanggal_mulai']
        }
        return render(request, 'dashboard-umpire.html', context)
    else:
        # unauthorized page view
        logger.info('C')
        raise Exception


# # DASHBOARD with data from database
# def dashboard_atlet_by_id(request, id):
#     data = query(
#         f"""
#         SELECT m.nama, m.email, a.*
#         FROM member m, atlet a
#         WHERE m.id = a.id
#         AND m.id='{id}'::uuid
#         """
#     )
#     context = {
#         'id': data[0]['id'],
#         'nama': data[0]['nama'],
#         'height': data[0]['height'],
#         'world_rank': data[0]['world_rank'],
#         'negara_asal': data[0]['negara_asal'],
#         'tgl_lahir': data[0]['tgl_lahir'],
#         'jenis_kelamin': data[0]['jenis_kelamin'],
#         'total_point': 0,
#         'email': data[0]['email'],
#         'pelatih': 'belum dihandle bang. ini nanti make string aggregation',
#         'status': 'belum handle jg. ini ntar cek dia udah kualifikasi atau blm',
#         'play_right': data[0]['play_right']
#     }
#     return render(request, 'dashboard-atlet-data.html', context=context)
# def dashboard_pelatih_by_id(request, id):
#     data = query(
#         f"""
#         SELECT m.nama, m.email, p.*
#         FROM member m, pelatih p
#         WHERE m.id = p.id
#         AND m.id='{id}'::uuid
#         """
#     )
#     context = {
#         'id': data[0]['id'],
#         'nama': data[0]['nama'],
#         'spesialisasi': 'ini blm dihandle. bakal make string aggregate',
#         'email': data[0]['email'],
#         'tanggal_mulai': data[0]['tanggal_mulai']
#     }
#     return render(request, 'dashboard-pelatih-data.html', context=context)
# def dashboard_umpire_by_id(request, id):
#     data = query(
#         f"""
#         SELECT m.nama, m.email, u.*
#         FROM member m, umpire u
#         WHERE m.id = u.id
#         AND m.id='{id}'::uuid
#         """
#     )
#     context = {
#         'id': data[0]['id'],
#         'nama': data[0]['nama'],
#         'email': data[0]['email'],
#         'negara': data[0]['negara']
#     }
#     return render(request, 'dashboard-umpire-data.html', context=context)

# REGISTER PENGGUNA
def register_pengguna(request):
    return render(request, 'register.html')
def register_atlet(request):
    return render(request, 'register-atlet.html')
def register_pelatih(request):
    return render(request, 'register-pelatih.html')
def register_umpire(request):
    return render(request, 'register-umpire.html')

# LOGIN
def login(request):
    if 'user_id' not in request.session:
        return render(request, 'login.html')
    else:
        return redirect('/authentication/dashboard-atlet')


def logout(request):
    request.session.flush()
    return redirect('/authentication/login')


def post_register_atlet(request):
    uid = uuid.uuid4()
    form = get_request_body(request)

    insert_member = f"""
        INSERT INTO MEMBER 
        VALUES ('{uid}', '{form['nama']}', '{form['email']}')
    """
    response = query(insert_member)

    if isinstance(response, int):
        insert_atlet = f"""
            INSERT INTO ATLET
            VALUES ('{uid}', '{form['tgl_lahir']}', '{form['negara_asal']}', 
                    '{form['play_right']}', {form['tinggi']}, 
                    NULL, '{form['jenis_kelamin']}')
        """
        query(insert_atlet)
        return redirect('/authentication/login')
    else:
        context = {
            'message': f"Email {form['email']} is already registered."
        }
        return render(request, 'register-atlet.html', context)


def post_login(request):
    form = get_request_body(request)
    validate = f"""
        SELECT id 
        FROM MEMBER 
        WHERE nama = '{form['nama']}' AND email = '{form['email']}'
        """
    response = query(validate)
    if isinstance(response, list) and len(response) > 0:
        logger.warning("A")
        role = get_user_role(response[0].get('id'))
        request.session['user_id'] = str(response[0].get('id'))
        request.session['user_role'] = role
        
        if role == 'ATLET': return redirect('/authentication/dashboard-atlet')
        elif role == 'PELATIH': return redirect('/authentication/dashboard-pelatih')
        elif role == 'UMPIRE': return redirect('/authentication/dashboard-umpire')

    else:
        return render(request, 'login.html', {'message': 'Nama/Email invalid.'})



def get_request_body(request):
    res = {}
    for param, body in request.POST.items():
        res[param] = body
    return res

# DASHBOARD ATLET UTILS
def get_user_role(uid):
    atlet = query(f"SELECT * FROM ATLET WHERE id = '{uid}'")
    if len(atlet) > 0: return 'ATLET'

    pelatih = query(f"SELECT * FROM PELATIH WHERE id = '{uid}'")
    if len(pelatih) > 0: return 'PELATIH'

    umpire = query(f"SELECT * FROM UMPIRE WHERE id = '{uid}'")
    if len(umpire) > 0: return 'UMPIRE'

def get_pelatih_atlet(uid):
    pelatih = query(f"""
        SELECT STRING_AGG(m.nama, ', ') AS PELATIH
        FROM atlet_pelatih a
        JOIN member m ON a.id_pelatih = m.id
        WHERE a.id_atlet = '{uid}'
    """)
    if not isinstance(pelatih, list): return '-'
    else: return pelatih[0].get('pelatih')

def get_status_atlet(uid):
    status = query(f"""
        SELECT * FROM atlet_kualifikasi
        WHERE id_atlet = '{uid}'
    """)
    if not isinstance(status, list): return 'Not Qualified'
    else: return 'Qualified'

def get_total_point(uid):
    total_point = query(f"""
        SELECT total_point FROM point_history
        WHERE id_atlet = '{uid}'
    """)
    if not isinstance(total_point, list): return 0
    else: return total_point[0].get('total_point')