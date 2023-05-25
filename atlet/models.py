
from django.db import models


class Atlet(models.Model):
     nama = models.CharField(max_length=255)

     def __str__(self):
         return self.nama
    
# class Stadium(models.Model):
#     nama = models.CharField(max_length=50, primary_key=True)
#     alamat = models.CharField(max_length=50)
#     kapasitas = models.IntegerField()
#     negara = models.CharField(max_length=50)

#     class Meta:
#         db_table="stadium"

# class Event(models.Model):
#     nama_event = models.CharField(max_length= 50, primary_key=True)
#     tahun = models.IntegerField()
#     nama_stadium = models.ForeignKey(Stadium, on_delete= models.CASCADE, related_name='stadium_nama')
#     negara = models.CharField(max_length=50)
#     tgl_mulai = models.DateTimeField()
#     tgl_selesai = models.DateTimeField()
#     kategori_superseries = models.CharField(max_length=50)
#     total_hadiah = models.BigIntegerField()

#     class Meta:
#         db_table="event"

# class Partai_kompetisi(models.Model):
#     jenis_partai = models.CharField(max_length=2, primary_key=True) 
#     nama_event = models.ForeignKey(Event, on_delete= models.CASCADE, related_name='partai_kompetisi_nama_event')
#     tahun_event = models.ForeignKey(Event, on_delete= models.CASCADE, related_name='partai_kompetisi_tahun')

#     class Meta:
#         db_table="partai_kompetisi"
    
# class Spesialisasi(models.Model):
#     id = models.UUIDField(primary_key=True)
#     spesialisaso = models.CharField(max_length=20)
    
#     class Meta:
#         db_table="spesialisasi"






# Create your models here.
