from abc import ABC, abstractmethod
import os
class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = 2023 - tahun_daftar
        self.saldo = saldo
        
    @abstractmethod
    def transfer_saldo(self, jumlah):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
    def lihat_saldo(self):
        print(f"Saldo {self.nama}: {self.saldo}")

class AkunGold(AkunBank):
    def transfer_saldo(self, jumlah):
        biaya_admin = 0
        
        if self.tahun_daftar <= 3 and jumlah > 100000:
            biaya_admin = 2000
        elif self.tahun_daftar > 3 and jumlah > 100000:
            biaya_admin = 0
        
        total_transfer = jumlah + biaya_admin
        if self.saldo >= total_transfer:
            self.saldo -= total_transfer
            print(f"Transfer {jumlah} berhasil. Biaya administrasi: {biaya_admin}. Saldo {self.nama} sekarang: {self.saldo}")
        else:
            print(f"Transfer gagal. Saldo {self.nama} tidak mencukupi")
    
    def lihat_suku_bunga(self):
        if self.tahun_daftar > 3 and self.saldo >= 1000000000:
            bunga = 0.01
            self.saldo = self.saldo + self.saldo* bunga
            print(f"suku bunga anda adalah {bunga}% saldo anda ditambah suku bungan adalah {self.saldo}")
        elif self.tahun_daftar <= 3 and self.saldo >= 1000000000:
            bunga = 0.02
            self.saldo = self.saldo + self.saldo* bunga
            print(f"suku bunga anda adalah {bunga}% saldo anda ditambah suku bungan adalah {self.saldo}")
        else:
            bunga = 0.03
            self.saldo = self.saldo + self.saldo* bunga
            print(f"suku bunga anda adalah {bunga}% saldo anda ditambah suku bungan adalah {self.saldo}")

class AkunSilver(AkunBank):
    def transfer_saldo(self, jumlah):
        biaya_admin = 0
        
        if self.tahun_daftar <= 3 and jumlah > 100000:
            biaya_admin = 5000
        elif self.tahun_daftar > 3 and jumlah > 100000:
            biaya_admin = 2000
        
        total_transfer = jumlah + biaya_admin
        if self.saldo >= total_transfer:
            self.saldo -= total_transfer
            print(f"Transfer {jumlah} berhasil. Biaya administrasi: {biaya_admin}. Saldo {self.nama} sekarang: {self.saldo}")
        else:
            print(f"Transfer gagal. Saldo {self.nama} tidak mencukupi")
    
    def lihat_suku_bunga(self):
        if self.tahun_daftar > 3 and self.saldo >= 10000000:
            bunga = 0.01
            self.saldo = self.saldo + self.saldo* bunga
            print(f"suku bunga anda adalah {bunga}% saldo anda ditambah suku bungan adalah {self.saldo}")
        elif self.tahun_daftar <= 3 and self.saldo >= 10000000:
            bunga = 0.02
            self.saldo = self.saldo + self.saldo* bunga
            print(f"suku bunga anda adalah {bunga}% saldo anda ditambah suku bungan adalah {self.saldo}")
        else:
            bunga = 0.03
            self.saldo = self.saldo + self.saldo* bunga
            print(f"suku bunga anda adalah {bunga}% saldo anda ditambah suku bungan adalah {self.saldo}")        

os.system("cls")
bank_1 = AkunGold("paijo", 2020, 5000000)
bank_2 = AkunSilver("maritim", 2019, 1000000)
bank_1.lihat_suku_bunga()
bank_1.transfer_saldo(100000)
bank_1.lihat_saldo()
bank_2.lihat_suku_bunga()
bank_2.transfer_saldo(1000000)
bank_2.lihat_saldo()