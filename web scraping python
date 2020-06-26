from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from urllib.request import urlopen
import re
import requests
haberler_csv = []
haberler_xml = []
r = requests.get('http://rss.haberler.com/rss.asp')
source = BeautifulSoup(r.content,'html.parser')
haberler_xml = source.find_all('item')
cumleler = []
for i in haberler_xml:
    haber = BeautifulSoup(str(i),"html.parser")
    url = haber.find("guid").get_text()
    #print(haber.find("title").get_text(),"\n" ,url)
    haber_metni = BeautifulSoup(requests.get(url).content,"html.parser").find("div",{"class":"haber_metni"}).get_text()
    #print(haber_metni)
    parca = re.sub(r"\[\d+\]", " ", haber_metni)
    parca = re.sub(r"\[", " ", parca)
    parca = re.sub(r"\]", " ", parca) #buraları d
    parca = re.sub(r"\(", " ", parca)
    parca = re.sub(r"\)", " ", parca)
    parca = re.sub(r"[:,'\"-]", " ", parca)
    parca = re.sub(r"\s+", " ", parca)
    haber_metni = parca.strip()
    tmp_cumleler = sent_tokenize(haber_metni)
    segment_no=0
    for cumle in tmp_cumleler:
        segment_no=segment_no+1
        cumle = str(cumle).replace(";"," ")
        cumleler.append([url,segment_no, cumle, len(word_tokenize(cumle))])
csv = open("corpus.csv", 'w+', encoding='utf-8')
csv.write("url;segment_no;cumle_icerigi;kelime_sayisi\n")
alinan_sözcükler = ""

for cumle in cumleler:
    alinan_sözcükler = alinan_sözcükler + str(cumle[0]) + ";"
    alinan_sözcükler = alinan_sözcükler + str(cumle[1]) + ";"
    alinan_sözcükler = alinan_sözcükler + str(cumle[2]) + ";"
    alinan_sözcükler = alinan_sözcükler + str(cumle[3]) + ";"
    alinan_sözcükler = alinan_sözcükler + "\n"
print("Basarili")
csv.write(str(alinan_sözcükler))
csv.close()

