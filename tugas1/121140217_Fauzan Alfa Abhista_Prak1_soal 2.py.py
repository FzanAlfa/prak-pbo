username = "informatika"
password = "12345678"

for i in range(0,3):
    input_1 = input("Username anda : ")
    input_2 = input("Username anda : ")
    if input_1 == username and input_2 == password:
        print("Berhasil login!")
        break
    else:
        if i == 2:
            print("anda sudah melakukan 3 kali percobaan gagal, akun anda diblokir")
        else:
             print("Username atau password salah coba lagi")