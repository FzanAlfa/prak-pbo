import os
class AkunBank:
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.nama_pelanggan = nama_pelanggan
        self.no_pelanggan = no_pelanggan
        self.__jumlah_saldo = jumlah_saldo #atribut privat
    
    def lihat_saldo(self):
        print(f"saldo anda saat ini adalah : {self.__jumlah_saldo}")

    def tarik_tunai(self, jumlah_uang):
        if jumlah_uang <= self.__jumlah_saldo:
            self.__jumlah_saldo -= jumlah_uang
            print(f"tarik tunai senilai {jumlah_uang} berhasil")
            print(f"saldo anda saat ini adalah {self.__jumlah_saldo}")
        else:
            print(f"jumlah uang anda tidak mencukupi!")

    def transfer(self, penerima, jumlah_uang):
        if jumlah_uang <= self.__jumlah_saldo:
            self.__jumlah_saldo -= jumlah_uang
            penerima.__jumlah_saldo += jumlah_uang #penambahan saldo ke rekening tujuan
            print(f"transfer senilai {jumlah_uang} ke {penerima.nama_pelanggan} berhasil")
            print(f"saldo anda saat ini adalah {self.__jumlah_saldo}")
        else:
            print(f"jumlah uang anda tidak mencukupi!")

os.system("cls")
Akun1 = AkunBank(1234, "fauzan alfa abhista", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)
base_akun = [Akun1, Akun2, Akun3] #list untuk data ke 3 akun
print(f"""Selamat datang di Bank Jago
mohon untuk login terlebih dahulu!""")
login_no = int(input("masukan no pelanggan : ")) #input no pelanggan
login_nama = input("masukan nama pelanggan : ") #input nama pelanggan

for akun in base_akun:
    if akun.nama_pelanggan == login_nama and akun.no_pelanggan == login_no: #validasi login
        validasi = True
        while True:
            print("Selamat data di bank jago!")
            print(f"""Halo {akun.nama_pelanggan}, ingin melakukan apa?
1. Lihat saldo
2. Tarik tunai
3. Transfer saldo
4. Keluar""") #menu
            masukan = int(input("Masukkan nomor input: "))
            if (masukan == 1):
                akun.lihat_saldo()
            elif(masukan == 2):
                jumlah_tarik = int(input("masukan jumlah tarik tunai : "))
                akun.tarik_tunai(jumlah_tarik)
            elif(masukan == 3):
                jumlah_transfer = int(input("masukan jumlah uang yang ingin ditranfer : "))
                no_tujuan = int(input("masukan no pelanggan tujuan : "))
                for akun_tujuan in base_akun: #perulangan for untuk mengetahui akun tujuan
                    if akun_tujuan.no_pelanggan == no_tujuan:
                        akun.transfer(akun_tujuan, jumlah_transfer)
            elif(masukan == 4):
                break
        break
#   else:
#       validasi = False
 