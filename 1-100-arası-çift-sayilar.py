# 1-100 arası Çift Sayıları Listeleyen Python Kodunu Ve Algoritmasını Yazınız.
 
# 1 birden yüze kadar olan sayıları for döngüsyle yazdır
# 2 yazdırılan heer bir sayıyı ikiyle mod alarak tek veya çift olarak ayır
# 3 modu sıfır olan yani çift olan sayıları ekrana yazdır


for i in range(1,101):
    if i%2==0:
        print(i)