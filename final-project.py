'''
Nesne tabanlı programlamayı burada yapmak isterdim fakat daha öğreneceklerim var :d
'''

import random as rnd

name = "emirhan"
lastname = "gümüş"

giris = 0
i = 2

# Giriş
while i > -1:
    print("***** GİRİŞ FORMU *****")
    user_name = input("Adınız (emirhan): ")
    user_lastname = input("Soyadınız (gümüş): ")
    if user_name == name and lastname == user_lastname:
        print("Başarıyla Giriş Yapıldı.")
        giris = 1
        break
    else:
        print("Hatalı giriş. {} hakkınız kaldı".format(i))
        i -= 1
        continue
else:
    print("Lütfen daha sonra tekrar deneyin.")
    exit() 

# Tanımlanması Gereken Değişkenler
dersler = []
i = 0
ders_sayisi = len(dersler)

def dersEkle():
    x = input("Dersleri Ekle (Boşluklarla): ")
    global dersler
    dersler = x.split()

def merhaba():
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
    print("Hoşgeldin {}!".format(name))

def notKontrol(x):
    if 0 > x:
        print("Negatif sayı alamaz. Sistem Kapanıyor...")
        exit()
    elif 100 < x:
        print("100'den büyük sayı alamaz. Sistem kapanıyor...")
        exit()
    else:
        None


if 1 == giris:
    merhaba()
    dersEkle()
    while True:
        if 3 <= len(dersler) <= 5:
            print("Dersler başarıyla eklendi.")
            break
        elif 3 > len(dersler):
            print("Yetersiz ders sayısı. Sınıfta kaldınız.")
            exit()
        else:
            print("Maksimum ders sayısı aşıldı. Lütfen tekrar giriniz.")
            dersEkle()
            continue
    randomDers = (rnd.choice(dersler))
    arasınav = int(input("{} dersinden aldığınız ara sınavdan notu giriniz: ".format(randomDers)))
    notKontrol(arasınav)
    final = int(input("{} dersinden aldığınız final notunuzu giriniz: ".format(randomDers)))
    notKontrol(final)
    proje = int(input("{} dersinden aldığınız proje notunuzu giriniz: ".format(randomDers)))
    notKontrol(proje)
    dersnotlari = {
        "Ara Sınav": arasınav,
        "Final": final,
        "Proje": proje,
    }
    print(randomDers + " dersinden aldığınız notlar: " + str(dersnotlari))
    puan = arasınav * 0.3 + final * 0.5 + proje * 0.2
    if 90 < puan:
        print("Puanınız: AA / {}".format(puan))
    elif 70 < puan < 90:
        print("Puanınız: BB / {}".format(puan))
    elif 50 < puan < 70:
        print("Puanınız: CC / {}".format(puan))
    elif 30 < puan < 50:
        print("Puanınız: DD / {}".format(puan))
    elif puan < 30:
        print("Puanınız: FF / {}".format(puan))
        print("Geçemediniz.")
else:
    print("Bilinmeyen Hata")