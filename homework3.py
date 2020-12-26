'''
İlk kez ciddi şekilde bir yazılım dilinde programlama yapıyorum. Çokça hatalar vardır bu kodda da ama güzel oldu bence :)
'''

import random as rnd

# Kullanıcı Adı Alma

username = input("Kullanıcı Adınızı Giriniz: ")
print("Hoşgeldin {}! Oyuna hazır mısın? (e/h)".format(username))

# Oyuna Hazırlık
while True:
    isReady = input()
    start = 0
    if "e" == isReady:
        print("Başlayalım o halde.")
        start += 1
        break
    elif "h" == isReady:
        print("Tamam, gidiyorum o zaman ben.")
        exit()
    else:
        print("Anlamadım. Tekrarlar mısın?")
        continue


# Rastgele Kelime Seçimi
randomKategori = ["hayvanlar", "nesneler", "şehirler"]
kategori = (rnd.choice(randomKategori))
if "hayvanlar" == kategori:
    kelimeListesi = ["köpek", "kedi", "inek", "tavşan", "balık", "kurbağa", "aslan"]
    kelime = rnd.choice(kelimeListesi)
elif "nesneler" == kategori:
    kelimeListesi = ["bardak", "bilgisayar", "kitap", "yastık", "kalem", "telefon"]
    kelime = rnd.choice(kelimeListesi)
elif "şehirler" == kategori:
    kelimeListesi = ["samsun", "istanbul", "ankara", "kırıkkale", "nevşehir", "bursa", "mardin", "diyarbakır"]
    kelime = rnd.choice(kelimeListesi)
else:
    print("Bilinmeyen Hata")
    exit()

# Değişken Tanımlamaları
kelime_uzunlugu = len(kelime)
adam_can = 10
print(kelime)
i = 0
gizli_kelime_0 = []

# Kelimeyi Listeye Diz
while i != kelime_uzunlugu:
    a = kelime[i]
    gizli_kelime_0.append(a)
    i += 1

i = 0 # Küçük Bir Reset İşlemi
gizli_kelime_1 = gizli_kelime_0.copy() # Listeyi Kopyala

# Kelimeyi Gizle
while i != kelime_uzunlugu:
    gizli_kelime_1[i] = '_'
    i += 1

# Oyun
while True:
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
    print("***** Oyunumuzun Adı: Adam Asmaca! *****")
    print("Kategori: {}. {} harfli bir kelime. {} yanlış bilme hakkın var.".format(kategori, kelime_uzunlugu, adam_can))
    print("Adamımızın canı {} kaldı!".format(adam_can))
    print("*********************")
    print("{} \n ".format(gizli_kelime_1))
    print("*********************")
    if adam_can == 0:
        print("Adam Öldü. Kelime {} idi.".format(kelime))
        break
    else:
        konsol1 = input("Tahminde bulunmak için '1', harf için '2' yazınız: ") # Tahmin ya da Harf İstemi
        if "1" == konsol1:
            kull_tahmin = input("Tahmininiz nedir: ")
            if kull_tahmin == kelime:
                print("Tebrikler doğru cevap! Kelime {} idi!".format(kelime))
                break
            else:
                print("Yanlış tahmin! Adamın canı bir eksildi!")
                adam_can -= 1
                print("Kalan can: {}".format(adam_can))
                continue
        elif "2" == konsol1:
            kull_harfi = input("Harf giriniz: ")
            if kull_harfi in kelime:
                print("{} harfi kelimede var!".format(kull_harfi))
                while kull_harfi in gizli_kelime_0:
                    harf_index1 = gizli_kelime_0.index('{}'.format(kull_harfi))
                    gizli_kelime_1[harf_index1] = kull_harfi
                    gizli_kelime_0[harf_index1] = "_"
                continue
            else:
                adam_can -= 1
                print("{} kelimede yok. Adamınızın canı {} kaldı.".format(kull_harfi, adam_can))
                continue
        else:
            print("Bilinmeyen Hata")
            continue