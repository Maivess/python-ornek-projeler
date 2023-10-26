# kullanıcıdan alınan 10 sayıdan en küçüğünü bul 
# 1 en küçük sayiyi belirle 
# 2 kullanıcıdan for döngüsüyle 10 tane sayı al 
# 3 alınan her bir sayıyı elimizdeki en küçük değer ile kıyasla 
# 4 yeni sayı eski en küçük sayıdan büyükse sıradaki sayıya geç 
# 5 yeni sayı eski en küçük sayıdan küçükse yeni sayıyı en küçük değer olarak ata ve sıradaki sayıya geç


min = 1

for i in range(10):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    if  sayi < min:
        min = sayi

print(f"En küçük sayı: {min}")