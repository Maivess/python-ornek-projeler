# kullanıcıdan sayı alınır.
# sayının pozitif olup olmadığı incelenir.
# sayı 1 ise asal olmadığı belirtilir.
# sayı 2 ise asal olduğu belirtilir.
# sayı ikiden büyükse iki sayısından sayının kendisine kadar olan bütün sayılar bölen olacak şekilde özyinelemeli bir biçimde artılır.
# eğer girilen sayı 2 den kendi değerine kadar olan hiç bir sayıya tam bölünmüyorsa sayının asl olduüu belirtilir.
# eğer girilen sayıyı tam bölen bir değer bulunursa sayının asal olmadığı belirtilir. 



def asal_mi(n, bolen=2):
    if n < 2:
        return False
    if n == 2 or bolen == n:
        return True
    if n % bolen == 0:
        return False
    else:
        return asal_mi(n, bolen + 1)


try:
    sayi = int(input("Bir sayi girin: "))
    if sayi < 0:
        print("Lutfen pozitif bir sayi girin.")
    elif asal_mi(sayi):
        print(f"{sayi} sayisi asaldir.")
    else:
        print(f"{sayi} sayisi asal değildir.")
except ValueError:
    print("Gecersiz bir sayi girişi yaptiniz.")
