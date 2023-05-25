import uuid
from django.db import models


# Create your models here.

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nama = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class Meta:
        db_table="member"


class Atlet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    tgl_lahir = models.CharField(max_length=100)
    negara_asal = models.CharField(max_length=100)
    play_right  = models.BooleanField()
    height = models.IntegerField()
    world_rank = models.IntegerField()
    jenis_kelamin = models.BooleanField()

    class Meta:
        db_table="atlet"

class Point_history(models.Model):
    id_atlet = models.UUIDField(primary_key=True, default=uuid.uuid4)
    minggu_ke = models.IntegerField()
    bulan = models.CharField(max_length=20)
    tahun  = models.IntegerField()
    total_point = models.IntegerField()
    
    class Meta:
        db_table="point_history"

class Atlet_kualifikasi(models.Model):
    id_atlet= models.UUIDField(primary_key=True, default=uuid.uuid4)
    world_rank = models.IntegerField()
    world_tour_rank = models.IntegerField()
    class Meta:
        db_table="atlet_kualifikasi"

class Atlet_non_kualifikasi(models.Model):
    id_atlet= models.UUIDField(primary_key=True, default=uuid.uuid4)
    class Meta:
        db_table="atlet_non_kualifikasi"

class Atlet_ganda(models.Model):
    id_atlet_ganda = models.UUIDField(primary_key=True, default=uuid.uuid4)
    id_atlet_kualifikasi = models.UUIDField( default=uuid.uuid4)
    id_atlet_kualifikasi_2 = models.UUIDField(default=uuid.uuid4)

    class Meta:
        db_table="atlet_ganda"

class Event(models.Model):
    nama_event = models.CharField(max_length=50,primary_key=True)
    tahun = models.IntegerField()
    nama_stadium = models.CharField(max_length=50)
    negara = models.CharField(max_length=50)
    tgl_mulai = models.DateField()
    tgl_selesai = models.DateField()
    kategori_superseries = models.CharField(max_length=50)
    total_hadiah = models.BigIntegerField()
    class Meta:
        db_table="event"

class Partai_kompetisi(models.Model):
    jenis_partai = models.CharField(max_length=2)
    nama_event = models.CharField(max_length=50,primary_key=True)
    tahun_event = models.IntegerField()
    class Meta:
        db_table="partai_kompetisi"

class Stadium(models.Model):
    nama = models.CharField(max_length=50, primary_key=True)
    alamat = models.CharField(max_length=50)
    kapasitas = models.IntegerField()
    negara = models.CharField(max_length=50)
    class Meta:
        db_table="stadium"
