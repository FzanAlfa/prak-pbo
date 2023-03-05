import os
os.system("cls")
class Mahasiswa:
    def __init__(self, nama, nim, kelas_siakad, jumlah_sks):
        self.nama = nama
        self.nim = nim
        self.kelas_siakad = kelas_siakad
        self.jumlah_sks = jumlah_sks
    
    def print_data_diri(self):
        print(f"""
============= Data diri =============
Nama         : {self.nama}
Nim          : {self.nim}
kelas siakad : {self.kelas_siakad}
jumlah sks   : {self.jumlah_sks}
=====================================""")

    #main
data_1 = Mahasiswa("Fauzan Alfa Abhista", "121140217", "RD", "24")
data_1.print_data_diri()