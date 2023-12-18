import math

class HesapMakinesi:
    def topla(self, x, y):
        return x + y

    def cikar(self, x, y):
        return x - y

    def carp(self, x, y):
        return x * y

    def bol(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Bolme islemi sifira bolme hatasi"

    def faktoriyel(self, x):
        max_limit = 170 
        if x == 0 or x == 1:
            return 1
        elif x < 0 or not isinstance(x, int):
            return "Gecersiz giris. Pozitif bir tam sayi gerekir."
        elif x > max_limit:
            return "Siniri astiniz. Daha kucuk bir sayi deneyin."
        else:
            return math.factorial(x)

    def us_alma(self, x, y):
        max_limit = 10**100  
        try:
            result = x ** y
            if result <= max_limit:
                return result
            else:
                raise OverflowError("Result too large")
        except OverflowError as e:
            if "Result too large" in str(e):
                return "Siniri astiniz. Daha kucuk bir sayi deneyin."
            else:
                raise e
            
            

    def karekok(self, x):
        
            return x ** 0.5
    
    
        

    def mod_alma(self, x, y):
        if y != 0:
            return x % y
        else:
            return "Sifira bolme hatasi"


hesap_makinesi = HesapMakinesi()

while True:
    print("\n1. Toplama")
    print("2. Çikarma")
    print("3. Çarpma")
    print("4. Bolme")
    print("5. Faktoriyel")
    print("6. Us Alma")
    print("7. Karekok")
    print("8. Mod Alma")
    print("9. Çikis")

    secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")

    if not secim:
        print("Geçersiz giriş. Lütfen bir seçenek girin.")
        continue

    if secim == "9":
        print("Çikis yapiliyor...")
        break

    try:
        sayi1 = float(input("Birinci sayiyi giriniz: "))
        if secim != "5" and secim != "7":
            sayi2 = float(input("İkinci sayiyi giriniz: "))
    except ValueError:
        print("Geçersiz giriş. Lütfen sayi giriniz.")
        continue

    if secim == "1":
        print("Toplama: ", hesap_makinesi.topla(sayi1, sayi2))
    elif secim == "2":
        print("Çikarma: ", hesap_makinesi.cikar(sayi1, sayi2))
    elif secim == "3":
        print("Carpma: ", hesap_makinesi.carp(sayi1, sayi2))
    elif secim == "4":
        print("Bolme: ", hesap_makinesi.bol(sayi1, sayi2))
    elif secim == "5":
        print("Faktoriyel: ", hesap_makinesi.faktoriyel(int(sayi1)))
    elif secim == "6":
        print("Us Alma: ", hesap_makinesi.us_alma(sayi1, sayi2))
    elif secim == "7":
        print("Karekok: ", hesap_makinesi.karekok(sayi1))
    elif secim == "8":
        print("Mod Alma: ", hesap_makinesi.mod_alma(sayi1, sayi2))
    else:
        print("Gecersiz seçim. Lutfen 1-9 arasinda bir secim yapin.")
