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
            return "Bölme işlemi sifira bolme hatasi"

    def faktoriyel(self, x):
        max_limit = 170  # math.factorial() sınırı
        if x == 0 or x == 1:
            return 1
        elif x < 0 or not isinstance(x, int):
            return "Geçersiz giriş. Pozitif bir tam sayı gerekir."
        elif x > max_limit:
            return "Sınırı aştınız. Daha küçük bir sayı deneyin."
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
                return "Sınırı aştınız. Daha küçük bir sayı deneyin."
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
    print("4. Bölme")
    print("5. Faktöriyel")
    print("6. Üs Alma")
    print("7. Karekök")
    print("8. Mod Alma")
    print("9. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")

    if not secim.isdigit() or not (1 <= int(secim) <= 9):
        print("Geçersiz giriş. Lütfen 1 ile 9 arasında bir sayı girin.")
        continue

    secim = int(secim)

    if secim == 9:
        print("Çıkış yapılıyor...")
        break

    try:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        if secim != 5 and secim != 7:
            sayi2 = float(input("İkinci sayıyı giriniz: "))
    except ValueError:
        print("Geçersiz giriş. Lütfen sayı giriniz.")
        continue

    if secim == 1:
        print("Toplama: ", hesap_makinesi.topla(sayi1, sayi2))
    elif secim == 2:
        print("Çıkarma: ", hesap_makinesi.cikar(sayi1, sayi2))
    elif secim == 3:
        print("Çarpma: ", hesap_makinesi.carp(sayi1, sayi2))
    elif secim == 4:
        print("Bölme: ", hesap_makinesi.bol(sayi1, sayi2))
    elif secim == 5:
        print("Faktöriyel: ", hesap_makinesi.faktoriyel(int(sayi1)))
    elif secim == 6:
        print("Üs Alma: ", hesap_makinesi.us_alma(sayi1, sayi2))
    elif secim == 7:
        print("Karekök: ", hesap_makinesi.karekok(sayi1))
    elif secim == 8:
        print("Mod Alma: ", hesap_makinesi.mod_alma(sayi1, sayi2))
    else:
        print("Geçersiz seçim. Lütfen 1-9 arasında bir seçim yapın.")
