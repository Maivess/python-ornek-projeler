# Kullanıcıdan 5 adet sayı alarak bu sayıların çarpımını ekrana yazdıran algoritmayı tasarlayınız.


# 1 kullanıcıdan ilk sayıyı al
# 2 kullanıcıdan ikinci sayıyı al 
# 3 bu iki sayıyı çarp ve sonuc olarak ata 
# 4 üçüncü sayıyı al,sonucla çarp ve sonuca ata
# 5 dördüncü sayıyıda al ve sonucla çarpıp sonuca ata 
# 6 son sayıyı da alıp sonucla çarp ve sonuca ata 
# 7 sonucu ekrana yazdır



sayilar = []


for i in range(5):
    
    sayi = int(input(f"{i + 1}. sayiyi girin: "))
    
    
    sayilar.append(sayi)


sonuc = 1  

for sayi in sayilar:
    sonuc *= sayi


print("Girilen sayilarin çarpimi:", sonuc)