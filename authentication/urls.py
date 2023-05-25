from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
   
    path('', dashboard_atlet, name='dashboard-atlet'),
    path('dashboard-pelatih', dashboard_pelatih, name='dashboard-pelatih'),
    path('dashboard-umpire', dashboard_umpire, name='dashboard-umpire'),
    path('register-pengguna', register_pengguna, name='register-pengguna'),
    path('register-pengguna/atlet', register_atlet, name='register-atlet'),
    path('register-pengguna/atlet/post', post_register_atlet, name='register-atlet-post'),
    path('register-pengguna/pelatih', register_pelatih, name='register-pelatih'),
    path('register-pengguna/umpire', register_umpire, name='register-umpire'),
    path('login', login, name='login'),
    path('login/post', post_login, name='post-login'),
    path('logout', logout, name='logout'),
    # path('dashboard-atlet/<str:id>', dashboard_atlet_by_id, name='dashboard-atlet-by-id'),
    # path('dashboard-pelatih/<str:id>', dashboard_pelatih_by_id, name='dashboard-pelatih'),
    # path('dashboard-umpire/<str:id>', dashboard_umpire_by_id, name='dashboard-umpire-by-id'),
]