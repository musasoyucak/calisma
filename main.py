#değişkenler

haber = "haberiniz olsun"  #string


baslik = "haberiniz olsun"
vade = 12  #integer
faizOrani1 = 1.47  #float
faizOrani2 = 1.45
print(haber)
print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani1))

mesaj = "hoşgeldin"
musteriAdi = "musa"
musteriSoyadi = "soyucak"
sonucmesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi + "!"
print(sonucmesaj)
sayi1=10
sayi2=20
print(sayi1+sayi2)
print(sonucmesaj)

# if else şart
dolarDun = 7.65
dolarBugun = 7.55
if dolarDun < dolarBugun :
    print("Arttı")
if  dolarDun> dolarBugun :
    print("Azaldı")
if  dolarDun == dolarBugun:
    print("Esittir ")

    print("Bitti")

krediler=["hızlı kredi","maaşını halkbank'tan alanlar"," emekli ihtiyaç kredisi"]
    
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])


print(len(krediler)) #length
krediler[0]="çabuk kredi"
print(krediler)
#donguler
for kredi in krediler :
    print(kredi)
for i in range(10): 
       print(i)  # (10 kez)
for i in range(len(krediler)):
    print(i)

for i in range(len(krediler)):
    print(krediler[i])

for i in range(10):
    print(i)

for i in range(4,10):
    print(i)

for i in range(0,10,2):
    print(i)    


#FONKSİYONLAR
def kredileriListele():
    krediler = ["Hizli Kredi","Maasini Halkbank'tan Alanlara Özel","Mutlu Emekli İhtiyac Kredisi"]
    for kredi in krediler :
        print("<Option>"+kredi+"<Option>") 

kredileriListele() # fonsiyon çağırma
kredileriListele()
kredileriListele()
kredileriListele()