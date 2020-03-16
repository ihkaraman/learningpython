
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import urllib.request

toplam_resim = 0
resimsizliste = []

def excelyaz(rawurl, dosya, sayfa, ustsayfa):

    workbook = xlsxwriter.Workbook(dosya)
    worksheet = workbook.add_worksheet()
    row = 1

    while (sayfa <= ustsayfa):
        url = rawurl.format(sayfa)
        tablo = sayfatara(url)
        for i in range(0, len(tablo)):
            worksheet.write(row, 0, row)
            worksheet.write(row, 1, url)
            worksheet.write(row, 2, tablo[i].find_all("a")[0].text)
            worksheet.write(row, 3, tablo[i].find_all("a")[0].get("href"))
            worksheet.write(row, 4, tablo[i].find_all("p", {"class": "post-date"})[0].text)
            worksheet.write(row, 5, tablo[i].find_all("p", {"class": "post-author"})[0].text)
            row += 1
        print("{}. sayfa yazdırıldı.".format(sayfa))
        sayfa += 1

    workbook.close()
    print("İşlem tamamlandı.")


def sayfatara(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    veri = soup.find_all("div", {"class": "col1"})
    tablo1 = veri[0].contents
    return (tablo1[0].find_all("div", {"class": "post-header-overview"}))

def altsayfayiac(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    veriler = soup.find_all("a")
    resimlinkleri =[]
    resimlinkleri.clear()
    for veri in veriler:
        link = str(veri.get("href"))
        if (link.__contains__("pic.to/show")):
            resimlinkleri.append((link))
    return resimlinkleri

def resimbul(rawurl, sayfa, ustsayfa):

    while (sayfa <= ustsayfa):
        url = rawurl.format(ustsayfa)
        tablo = sayfatara(url)
        for i in range(0, len(tablo)):
            kategori = str(tablo[i].find_all("p", {"class": "post-author"})[0].text)
            if((kategori.__contains__("C")) or (kategori.__contains__("Movies"))):
                resimler = altsayfayiac(tablo[i].find_all("a")[0].get("href"))
                indirlink = resimlinkbul(resimler, tablo[i].find_all("a")[0].get("href"))
                # print(tablo[i].find_all("a")[0].get("href"))
                '''
                try:
                    resimindir(indirlink, tablo[i].find_all("a")[0].text)
                except (urllib.error.URLError, TimeoutError, requests.exceptions.ConnectionError):
                    print("Dosya indirilemedi, tekrar deneniyor")
                    print(i)
                    i -= 1
                    print(i)
                '''

        print("{}. sayfa incelendi.".format(ustsayfa))
        ustsayfa -= 1
    reimsizleriyaz()
    print(toplam_resim, " adet resim indirildi.")

def resimlinkbul(liste, isim2):
    indirmelinki = []
    indirmelinki.clear()
    for item in liste:
        r = requests.get(item)
        soup = BeautifulSoup(r.content, "html.parser")
        veriler = soup.find_all("div", {"class":"image"})
        if(len(veriler)==0):
            global resimsizliste
            resimsizliste.append(isim2)
            continue
        ress = str(veriler[0].contents[1].get("src"))
        indirmelinki.append(ress)
    return indirmelinki

def resimkontrol(liste):

    for item in liste:
        r = requests.get(item)
        soup = BeautifulSoup(r.content, "html.parser")
        veriler = soup.find_all("div", {"class": "image"})
        if (len(veriler) == 0):
            global resimsizliste
            resimsizliste.append(item)

def resimindir(linkler, isim):
    isim = isim
    say = 1
    for link in linkler:
        # print(link)
        urllib.request.urlretrieve(link, ("D:/games/" +isim + "_" + str(say) + ".jpg"))
        say += 1
        global toplam_resim
        toplam_resim += 1

def reimsizleriyaz():
    txt = open("resimsizler.txt", "w")
    for i in resimsizliste:
        txt.write(i)
        txt.write("\n")
    txt.close()

rawurl = "https://www/page/{}/"
dosya = "liste.xlsx"

altsayfa = 1
ustsayfa = 5


#excelyaz(rawurl, dosya, 2, ustsayfa)
resimbul(rawurl, altsayfa, ustsayfa)
reimsizleriyaz()
