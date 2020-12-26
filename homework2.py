kisi1 = list() #Liste Oluştur
kisi1_adi = input("Adınız: ") #Kişinin Adını Al
kisi1_soyadi = input("Soyadınız: ") #Kişinin Soyadını Al
kisi1_yas = int(input("Yaşınız: ")) #Kişinin Yaşını Al
kisi1_yil = int(input("Doğum Yılınız: ")) #Kişinin Doğum Yılını Al
kisi1.extend([kisi1_adi, kisi1_soyadi, kisi1_yas, kisi1_yil]) #Verileri listeye ekle

print("*****YOUR INFORMATIONS*****") #Sadece güzel gözüksün diye

for i in kisi1: #Kişinin Bilgilerini Ekrana Yazar
    print(i)

#Yaş Sorgulamasını Gerçekleştirir
if kisi1_yas < 0: #Sıfırdan Küçük İse Hata Verir
    print("Invalid Age")
elif kisi1_yas <= 18: #On Sekize küçük eşit ise
    print("You can't go out because it's too dangerous!")
else: #On Sekizden Yüksek İse
    print("You can go out to the street.")