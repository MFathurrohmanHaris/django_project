from django.db import models

# Create your models here.
class Provinsi(models.Model):
  id = models.CharField(max_length=2, primary_key=True)
  nama = models.CharField(max_length=100)
  
  def __str__(self):
    return self.nama
  
class KabupatenKota(models.Model):
  id = models.CharField(max_length=4, primary_key=True)
  provinsi = models.ForeignKey('Provinsi', on_delete=models.CASCADE)
  nama = models.CharField(max_length=100)
  
  def __str__(self):
    return self.nama
  
class Kecamatan(models.Model):
  id = models.CharField(max_length=7, primary_key=True)
  kabupatenKota = models.ForeignKey('KabupatenKota', on_delete=models.CASCADE)
  nama = models.CharField(max_length=100)
  
  def __str__(self):
    return self.nama
  
class Kelurahan(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  kecamatan = models.ForeignKey('Kecamatan', on_delete=models.CASCADE)
  nama = models.CharField(max_length=100)
  
  def __str__(self):
    return self.nama

class Anggota(models.Model):
  id = models.AutoField(primary_key=True)
  nama = models.CharField(max_length=100)
  jk = (
    (0, "Tidak memilih"),
    (1, "Laki-laki"),
    (2, "Perempuan")
  )
  jenis_kelamin = models.IntegerField(choices=jk, default=0)
  tempat_lahir = models.CharField(max_length=100)
  tgl_lahir = models.DateField()
  no_telp = models.CharField(max_length=20)
  provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE, blank=False)
  kabupaten_kota = models.ForeignKey(KabupatenKota, on_delete=models.CASCADE, blank=False)
  kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE, blank=False)
  kelurahan = models.ForeignKey(Kelurahan, on_delete=models.CASCADE, blank=False)
  