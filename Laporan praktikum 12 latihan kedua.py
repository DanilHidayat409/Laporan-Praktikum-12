# -*- coding: utf-8 -*-
"""
@Hari/Tanggal : Selasa,141221
@Judul : Laporan Praktikum 12
@Materi : Program OOP
@author: Muhammad Danil Hidayat
@NIM : 06500210032
"""

class mahasiswa:

 def __init__(self,nilai,nama):

   self.nilai = nilai
   self.nama = nama

 def ubah(self):

   print("Nama Kamu Adalah : " + self.nama)
   print("nilai kamu adalah : " + str(self.nilai))


perulangan = 0
while perulangan == 0 :

 print("\n==== Program OOP ==== ")
 print("1.Mendeklarasikan Objek")
 print("2.Menampilkan Objek")
 print("3.Mengganti Objek")
 print("4.Menghapus Objek")
 print("5.Menutup Program")

 pilihan = int(input("Masukan Pilihan kamu (1/2/3/4/5) : "))

 if pilihan == 1 :

    nama = str(input("Masukan Nama Kamu : "))
    nilai = str(input("Masukan Nilai Kamu : "))
    biodata = mahasiswa(nilai,nama)
    print("Data Berhasil Ditambahkan")

 elif pilihan == 2 :

    biodata = mahasiswa(nilai,nama)
    biodata.ubah()

 elif pilihan == 3 :

    a = "nama"
    b = "nilai"


 print("A : Nama")
 print("B : Nilai")
 perubahan = input("masukan pilihan : ")

 if perubahan == "a":

    nama = (input("masukan Nama yang ingin dirubah : "))

    print("Nama Berhasil Dirubah")

 elif perubahan == "b":

    nilai = (input("masukan nilai yang ingin dirubah : "))

 print("Nilai Berhasil Dirubah")