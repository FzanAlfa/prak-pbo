import random
import os

class Kotak:
    def __init__(self):
        self.isi = 'bom' if random.random() < 0.25 else 'kosong' #persentase munculnya bom adalah sebesar 25%
        self.status = 'belum'
    
    def tampilkan(self):
        if self.status == 'belum':
            return '?'
        elif self.isi == 'bom':
            return 'x'
        else:
            return 'o'
    
    def buka_kotak(self):
        self.status = 'sudah'
        
os.system("cls")
dimensi = int(input("Masukkan dimensi area: "))
menang = dimensi*dimensi-1
hitung = 0
area = []
for i in range(dimensi):
    row = []
    for j in range(dimensi):
        row.append(Kotak())
    area.append(row)

for row in area:
        print(' '.join(k.tampilkan() for k in row)) #print jumlah kotak 
while True:
    
    nomor_kotak = int(input("Masukkan nomor kotak yang ingin dibuka (1-{}): ".format(dimensi**2)))
    
    row = (nomor_kotak-1) // dimensi
    col = (nomor_kotak-1) % dimensi
    
    kotak = area[row][col]
    kotak.buka_kotak()
    
    if kotak.isi == 'bom':
        print("Game over! Kotak tersebut berisi bom.")
        for row in area:
            print(' '.join(k.tampilkan() for k in row))
        break
    else:
        hitung += 1
        if hitung == menang:
            print("Selamat! Anda telah memenangkan game.")
            for row in area:
                print(' '.join(k.tampilkan() for k in row))
            break
        else:
            for row in area:
                print(' '.join(k.tampilkan() for k in row))
            