# Verilen metnin ilk 15 ve son 15 karakterini gösterin

# 1 metni yaz 
# 2 metnin uzunluğunu "length" fonksiyonunu kullanarak bul 
# 3 ilk 15 karakteri yazdır
# 4 son 15 karakteri yazdır 

metin = "Merhaba benim adim Emre Uzun 21 yasindayim"

length = len(metin)

print(metin[0:15])
print(metin[length-16:length])