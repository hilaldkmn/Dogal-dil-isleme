import re
from collections import Counter
from nltk import word_tokenize
tum_kelimeler = []
with open('corpus.csv', mode='r', encoding="utf-8") as csv_dosyasi:
    csv_okuma = [i.split(";")[2].lower() for i in csv_dosyasi.read().split("\n")]
    for satir in csv_okuma:
        for kelime in word_tokenize(satir):
            tum_kelimeler.append(kelime)

tum_kelimeler = Counter(tum_kelimeler)

def kelime_siralamasi(kelime, N=sum(tum_kelimeler.values())): #bu fonksiyonda kelimenin ne kadar fazla geçme sıklığına bakıyoruz
    return tum_kelimeler[kelime] / N

def duzeltme(kelime): #bu fonksiyonda en fazla geçen kelimeye bakıyoruz
    return max(kelime_cogaltma(kelime), key=kelime_siralamasi)

def kelime_cogaltma(kelime): #bu fonksiyonda kelimenin yakın bağdaşık kelimeleri oluşturulması veya kelime zaten tanımlanmış ise çıktı verir
                         #kelime tanımda yoksa bağdaşık olan kelimelerden bulunma
    return (bilinen_kelimeler([kelime]) or bilinen_kelimeler(islem1(kelime)) or bilinen_kelimeler(islem2(kelime)) or [kelime])


def bilinen_kelimeler(kelimeler): #bu fonksiyonda kelimeler bağdaşıklığından bilinmesi ile bulunan kelimeler
    return set(w for w in kelimeler if w in tum_kelimeler)

def islem1(kelime): #kelimeye bir adım yakın olarak benzeşdirilen kelimelerin harfler ve kurallar ile oluşması
    harfler    = 'abcçdefgğhıijklmnoöprsştuüvyz'
    splits     = [(kelime[:i], kelime[i:])    for i in range(len(kelime) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in harfler]
    inserts    = [L + c + R               for L, R in splits for c in harfler]
    return set(deletes + transposes + replaces + inserts)

def islem2(kelime): #kelimeye iki adım yakın olarak benzeşdirilen kelimelerin islem1 adımlar ile oluşması
    return (e2 for e1 in islem1(kelime) for e2 in islem1(e1))

if __name__ == '__main__':
    print(duzeltme("türrkiyee"))
