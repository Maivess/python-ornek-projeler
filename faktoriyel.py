# girilen sayının faktoriyelini bulan kodu ve algoritmasını yazdırın 


# 1 kullanıcıdan sayı isteyin 
# birden alınan sayıya kadar olan sayıları for döngüsüyle yazıp çarpın
# 3 sonucu ekrana yazdırın 



sayi = int(input("Faktoriyelini hesaplamak istediğiniz sayiyi girin: "))

faktoriyel = 1

for i in range(1, sayi + 1):
        faktoriyel *= i
print(f"{sayi} faktoriyel = {faktoriyel}")
