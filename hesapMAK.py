sayi1=int(input("Sayı 1: "))
sayi2=int(input("Sayı 2: "))
toplam=sayi1+sayi2
print("Toplam:",toplam)

bolme=sayi1/sayi2
print("Hatalı bölme:",bolme)

try:
    bolum = sayi1/sayi2
    print("Bölüm:",bolum)
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz.")