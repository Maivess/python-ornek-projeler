# Kullanıcının  girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini 
# (VKİ=ağırlık/(boy*boy), boymetre cinsinden verilmeli) hesaplayınız.


# 1 kullanıcıdan metre cinsinden boy değeri girmesini iste ve bunu bir değişkene ata 
# 2 kullanıcıdan kilo değeri girmesini iste ve bunu bir değişkene ata 
# 3 kilo değerini boy değerinin metre cinsinden değerinin karesine böl
# 4 çıkan sonucu bir deişkene ata 
# 5 sonuc değişkeni 18-25 aralığındaysa "ideal aralıktasınız" yazdır
# 5 çıkan sonuc 25 ten fazlaysa "kilolusunuz" yazdır
# 6 çıkan sonuc 18 den azsa "zayıfsınız " yazdır 


boy = float(input ("boyunuzu giriniz (m)"))
kilo =float(input ("kilonuzu giriniz (kg)"))

sonuc = kilo/boy*boy 
if 18 <= sonuc <= 25:
    print("ideal araliktasiniz")
elif sonuc>25: 
    print("kilolusunuz")
elif sonuc<18:
    print("zayifsiniz")
