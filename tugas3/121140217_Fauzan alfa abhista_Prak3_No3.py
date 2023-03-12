import os
class Kendaraan: #Kelas Kendaraan adalah kelas dasar atau superkelas yang memiliki atribut kelas 
    jumlah_roda = 0 # Atribut kelas yang bernilai konsisten antar instance

    def __init__(self, merk, model, tahun_pembuatan):
        # Atribut instance yang bersifat private dan hanya dapat diakses melalui metode dalam kelas itu sendiri.
        self.__merk = merk
        self.__model = model
        self.__tahun_pembuatan = tahun_pembuatan
        self._warna = None # Atribut instance yang bersifat protected dan dapat diakses melalui metode dalam kelas itu sendiri maupun dalam subkelas.

    def tampilan_info(self):  # Fungsi instance yang bersifat public
        print(f"Merk: {self.__merk}")
        print(f"Model: {self.__model}")
        print(f"Tahun Pembuatan: {self.__tahun_pembuatan}")
        print(f"Jumlah Roda: {Kendaraan.jumlah_roda}")
        if self._warna is not None:
            print(f"Warna: {self._warna}")

    def _ubah_warna(self, warna_baru): # Fungsi instance yang bersifat protected
        self._warna = warna_baru

class Mobil(Kendaraan):
    def __init__(self, merk, model, tahun_pembuatan):
        super().__init__(merk, model, tahun_pembuatan)
        Kendaraan.jumlah_roda = 4
        self.jumlah_klakson = 0

    def klakson(self):  # Fungsi instance yang bersifat public
        print("Tin tin!")
        self.__jumlah_pencet_klakson()

    def __jumlah_pencet_klakson(self):  # Fungsi instance yang bersifat private
        self.jumlah_klakson += 1
        print(f"klakson yang dipencet sebanyak {self.jumlah_klakson}")

class Sepeda(Kendaraan):
    def __init__(self, merk, model, tahun_pembuatan):
        super().__init__(merk, model, tahun_pembuatan)
        Kendaraan.jumlah_roda = 2

    def belok_kiri(self): # Fungsi instance yang bersifat public
        print("Belok kiri!")

    def _ubah_warna(self, warna_baru):  # Fungsi instance yang bersifat protected
        print("Maaf, sepeda tidak bisa diubah warnanya")
os.system("cls")

kendaraan1 = Sepeda("united", "bmx", 2003)
kendaraan1.tampilan_info()
kendaraan1.belok_kiri()
kendaraan1._ubah_warna("jingga")
print("\n")
kendaraan2 = Mobil("sedan", "ndatau", 2022)
kendaraan2.tampilan_info()
kendaraan2.klakson()
kendaraan2.klakson()