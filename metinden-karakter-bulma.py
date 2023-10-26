#Verilen bir metinde istenilen karakterin kaç kere kullanıldığını bulan ve ekrana yazdıran kodu ve algoritmeyı yazınız

# 1 metni oluşturun 
# 2 kullanıcıdan hangi karakterin kaç kere tekrarladığını öğrenmek istediği bilgisini alın
# 3 count fonksiyonunu kullanarak istenen karakterin kaç kere tekrarladığını bulun
# 4 ekrana yazdırın 


metin ="Bugün python ile proglama yapmayı öğrenmeye başladım"

karakter= input("aramak istediğiniz karakteri girin ")

sonuc = metin.count(karakter)
print(sonuc)