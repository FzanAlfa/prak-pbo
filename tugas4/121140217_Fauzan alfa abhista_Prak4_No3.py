class Person:
    def __init__(self, gender, height, age):
        self.gender = gender
        self.height = height
        self.age = age

    def __add__(self, other): #overload dengan metode __add__ 
        return self.height + other.height

    def __sub__(self, other): #di-overload dengan metode __sub__
        return self.age - other.age

class Male(Person):
    def ideal_weight(self):
        # menghitung berat badan ideal untuk pria
        return 50 + 0.91 * (self.height - 152.4)

class Female(Person):
    def ideal_weight(self):
        # menghitung berat badan ideal untuk wanita
        return 45.5 + 0.91 * (self.height - 152.4)

p1 = Male('male', 175, 30)
p2 = Female('female', 160, float('25')) #casting dari char ke float
print(p1.ideal_weight()) # 70.45
print(p2.ideal_weight()) # 57.10
print(p1 + p2) # 335 #jumlah tinggi badan
print(p1 - p2) # 5 #selisih umur


