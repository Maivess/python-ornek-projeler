#Girilen vize ve final notuna göre öğrencinin dersten geçip geçemeyeceğini ekrana yazdıran algoritmayı ve kodu tasarlayınız


# 1 geçme notu isteyin
# 2 vize ağırlığını isteyin 
# 3 final ağırlığını bulun
# 4 vize notunu isteyin 
# 5 final notunu isteyin
# 6 vize notunu vize notu ağırlığıyla çarpıp "vizeEtkisi" değişkene atayın 
# 7 final notunu final notu ağırlığıyla çarpıp "finalEtkisi" değişkenine atayın
# 8 vizeEtkisi ve "finalEtkisi" değişkenini toplayıp sonuc değişkenine atayın
# 9 sonuc değişkenini geçme notuyla kıyaslayın
# 10 sonuc değişkeni geçme notundan büyükse veya geçme notuna eşitse "dersten geçilmiştir" yazdırın
# 11 sonuc değişkeni geçme notundan küçükse "dersten kalınmıştır" yazdırın



gecmeNotu = int(input("Gecme Notu :"))
vizeAgirlik = int(input("Vize Agirligi :"))
if 100 <= vizeAgirlik <= 0:
    print("geçersiz sayi girdiniz")

finalAgirlik = int(100-vizeAgirlik)

vizeNotu = float(input("Vize Notu :"))
if 100 <= vizeNotu <= 0:
    print("geçersiz sayi girdiniz") 


finalNotu = float(input("Final Notu :"))
if 100 <= finalNotu <= 0:
    print("geçersiz sayi girdiniz")

vizeEtkisi = (vizeNotu*vizeAgirlik/100)
finalEtkisi = (finalNotu*finalAgirlik/100)

sonuc = vizeEtkisi+finalEtkisi

if sonuc >= gecmeNotu:
    print("dersten geçilmiştir")
else :
    print("dersten kalınmıştır")