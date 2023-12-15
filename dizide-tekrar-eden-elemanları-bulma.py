# bir dizi oluşturulur.
# dizideki her bir eleman sırayla gezilir.
# eğer eleman zaten daha önceden unik değerlere eklenmişse tekrarlanana eklenir
# eğer eleman daha önce uniq e eklenmediyse uniq e eklenir.


dizi = [1, 2, 3, 4, 5, 2, 7, 8, 9, 1]

def tekrarlananlari_bul(dizi):
    tekrarlananlar = set()
    uniq_degerler = set()

    for eleman in dizi:
        if eleman in uniq_degerler:
            tekrarlananlar.add(eleman)
        else:
            uniq_degerler.add(eleman)

    return list(tekrarlananlar)



print("Tekrarlanan Elemanlar:", tekrarlananlari_bul(dizi))
