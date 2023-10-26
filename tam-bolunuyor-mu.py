# Girilen iki sayıdan ilkinin ikincisine tam bölünüp bölünmediğini bularak sonucu ekrana yazdıran algoritmayı tasarlayınız

# 1 kullanıcıdan birinci sayıyı al
# 2 kullanıcıdan ikinci sayıyı al
# 3 ilk sayıyı ikinci sayıya böl
# 4 tam bölünüyorsa "tam bölünüyor" yazıp bölümü yazdır






sayi1 = int(input("1. sayi:"))
sayi2 = int(input("2.sayi"))

sonuc = sayi1/sayi2

kalan = sayi1 % sayi2

if kalan == 0:
    print("ilk sayi ikinci sayiya tam bölünür")
else:
    print("ilk sayi ikinci sayiya tam bölünmez")    

print(f"{sayi1} / {sayi2} = {sonuc}")
