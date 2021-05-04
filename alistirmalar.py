
def calisan(**bilgiler):
    print("*"*30)
    print("SOYAD:",bilgiler["soyad"])
    print("sehir:",bilgiler["sehir"])
    print("Yas:",bilgiler["yas"])
    print("AD:",bilgiler["ad"])
    print("*"*30)
calisan(ad="Tugba",soyad="Kirac",yas=21,sehir="Kayseri")
calisan(ad="Huseyin",soyad="Can",yas=30,sehir="Ankara")
    
#Bilgileri karisik girsek de sorun olmaz.
# ** dikkat et!
#Bu sekilde cok sayida kullanicinin bilgilerini almis oluruz.

print("*"*30)
#BİR DİGER YONTEM 
def kayit_olustur(isim, soyisim, yas2, sehir2):
    print("-"*30)

    print("isim           : ", isim)
    print("soyisim        : ", soyisim)
    print("yas            : ", yas2)
    print("şehir          : ", sehir2)

    print("-"*30)
kayit_olustur("Tugba","Kirac","21","Kayseri")
kayit_olustur("Bulut","Can","20","Ankara")
