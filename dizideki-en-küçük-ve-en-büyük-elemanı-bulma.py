# dizi oluşturulur
# dizinin ilk elemanı hem maksimum hem minimum değer olarak atanır.
# ikinci eleman ilk hem maksimumla hem minimumla karşılaştırılır ve daha büyükse maksimum olarak küçükse minimum olarak atanır.
#işlem dizi elemanları bitene kadar devam eder.

dizi = [32, 1323, 4312, 213, 8444, 5123, 534, 68]


def min_max_bul(dizi):
    if not dizi:
        return None, None
    min_eleman = max_eleman = dizi[0]
    for eleman in dizi:
        if eleman < min_eleman:
            min_eleman = eleman
        elif eleman > max_eleman:
            max_eleman = eleman
    return min_eleman, max_eleman



min_eleman, max_eleman = min_max_bul(dizi)
print(f"En küçük eleman: {min_eleman}, en büyük eleman: {max_eleman}")
