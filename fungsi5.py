# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:34:38 2021

@author: zidan
"""

#fungsi sederhana
def fungsi():
    print('Fungsi Test')
    
fungsi()

#fungsi yang ribet juga
def harga(unit):
    harga = 5000000
    hargatotal = unit*harga
    print('harga', unit, 'Playstation adalah', hargatotal)
    
harga(2)

#fungsi dengan argumen
def mahasiswa(nama):
    print('Mahasiswa/i ini bernama:', nama)
    
#setiap bikin fungsi yang butuh input harus buat argumen
mahasiswa('Zidan')

#Fungsi dengan argumen 
def dosen(nama, matkul):
    print('Dosen ini bernama: ', nama)
    print('Mengajar matkul: ', matkul)
    
#digunakan untuk codingan dengan argumen yang panjang
dosen(nama='Nuraini', matkul='Bahasa Inggris')
dosen(matkul='Bahasa Inggris', nama='Nuraini')

dosen('Bahasa Inggris', 'Nuraini')

#fungsi menggunakan default arguments
def gurubk(nama, sifat='Tegas', galak='Banget'):
    print('Guru BK di sekolah ini bernama:', nama)
    print('Sifatnya:', sifat)
    print('Galak gak:', galak)

gurubk('Tri Cahyani')
gurubk('Suci Astuti', sifat='Baik', galak='Nggak')
#contoh argumen yang salah
gurubk(sifat='Neraka', galak='ampe ke inti bumi')

#fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari', argumen, 'adalah', total)
    #totalnya di return
    return total

#dengan argumen biasa
kuadrat(2)
x = kuadrat(5)
print(x)
print(kuadrat(3))

print('+'*100)

#fungsi dengan returnvalue dan mutiple argumen
def tambah(argumen1, argumen2, nice='nice'):
    total = argumen1 + argumen2
    print(argumen1, '+', argumen2, '=', total, nice)
    return total

x = tambah(35, 34)
print(x)

def kali(argumen1, argumen2):
    total = argumen1 * argumen2
    print(argumen1, 'x', argumen2, '=', total)
    return total

y = kali(60, 7)

z = kali(2, tambah(7, 9))

print(z)




#fungsi init
class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
        
    def do_work(self):
        if self.occupation == "Pegulat":
            print(self.name, "Gelud")
        elif self.occupation == "Aktor":
            print(self.name, "Drama")
                
    def speaks(self):
        print(self.name, "Bagaimana hari mu?")
        
zidan = Human ("Zidan Alamsyah", "Pegulat")
zidan.do_work()
zidan.speaks()


