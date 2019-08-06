"""
while(True):
    sayi = int(input("Bir sayı giriniz: "))
    print("Hesaplanıyor... ", sayi, "!")

    fakt = 1
    if (sayi > 0):
        i = 1
        for i in range(1, (sayi + 1)):
            fakt *= i
        print(sayi, "! = ", fakt)
    elif(sayi == 0):
        print(sayi, "! = ", fakt)
    elif(sayi == -99):
        break
    else:
        print("Negatif sayının faktöriyeli alınmaz.")


def metod(ad="bilgi yok", soyad="bilgi yok",numara="bilgi yok"):
    print(ad,soyad,numara)
print("selam")
metod("kitap","kalem")
metod(1,"kalem",5)
print("kitap\nkalem")



def toplamaFor(liste):
    toplam = 0
    for i in liste:
        toplam += i
    return toplam

def toplamaWhile(liste):
    toplam = 0
    i = 0
    while i < len(liste):
        toplam += liste[i]
        i += 1
    return toplam

def toplamaRec(liste):
    if(len(liste)>1):
        return liste[0] + toplamaRec(liste[1:])
    else:
        return(liste[0])

print("For: ",toplamaFor([1,2,3,4,5,6]))
print("While: ",toplamaWhile([1,2,3,4,5,6]))
print("Rec: ",toplamaRec([1,2,3,4,5,6]))

a = 10

def fonk():
    global a
    a = 3
    print(a)
print(a)

global degisken


sozluk = {"tanim1":"aciklama1", "tanim2":"aciklama2", "tanim3":"aciklama3"}
print(sozluk["tanim1"])

for i in sozluk.items():
    print(i)

for i in sozluk.items():
    print(i[0], " ", i[1] )
for i,j in sozluk.items():
    print(i + " " + j
          )
    print(i + " " + j)

import moduls

moduls.naber()
print(moduls.mutlak(-5))
import math

import urllib.request
url1 ="https://xyzt.jpg"
url2 ="https://images-na.ssl-images-amazon.com/images/I/41HwdEjD4XL._SY355_.jpg"
url3 ="https://www.andysemporium.co.uk/ekmps/shops/andy1/images/classic-designs-3-black-number-3-digit-pack-5-133612-p.jpg"

urllist = [url1, url2, url3]
say = 1
for i in urllist:
    urllib.request.urlretrieve(i, "resim" + str(say) + ".jpg")
    say += 1

# try, except

try:
    sayi1 = int(input("sayi1 "))
    sayi2 = int(input("sayi2 "))
    print(sayi1 / sayi2)
except ValueError:
    print("Hatalı sayı")
except ZeroDivisionError:
    print("Sıfıra bölünme hatası ")
finally:

# dosya işlemleri

dosya = open("dosya.txt", w)
dosya = open("dosya.txt", r)
dosya = open("dosya.txt", a)

dosya = open("deneme.txt", "w")
dosya.write("naber")
dosya = open("deneme.txt", "r")
print(dosya.readline())
dosya.close()



with open("deneme.txt", "r+") as dosya:
    data = dosya.read()
    data = "deneme1\n" + data
    dosya.seek(0)
    dosya.write(data)

    liste.insert(index, eklenecek_deger)



import sqlite3
con = sqlite3.connect("veritabani.db")
cursor = con.cursor()

def tabloOlustur():
   cursor.execute("CREATE TABLE IF NOT EXISTS TABLO (AD TEXT, SOYAD TEXT, DERS TEXT, NUMARA INT, NOTLAR FLOAT)")
   con.commit()
def degerEkle(ad= " - ", soyad= " - ", ders= " - ", ogrno = 0, not1 = 0.0):
   cursor.execute("INSERT INTO TABLO VALUES ('{}', '{}', '{}', {}, {}) ".format(ad, soyad, ders, ogrno, not1))
   con.commit()
tabloOlustur()
degerEkle("İsmail", "Karaman", "MAT01", 987766, 85.20)
degerEkle("İsmail", "Karaman", "END01", 987766, 89)
degerEkle("İsmail", "Karaman", "FIZ01", 987766)
degerEkle("Ali", "Atar", "MAT01", 975652, 75)
degerEkle(ad = "Ali", soyad = "Atar", ders = "FIZ01", not1 = 75)
con.close()

import sqlite3
import random
import time
import datetime

con = sqlite3.connect("dersler.db")
cursor = con.cursor()

def tablooluştur():
  cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (ZAMAN REAL, TARIH TEXT, ANAHTARKELIME TEXT,DEGER REAL)")

def rastgeledegerekle():
  zaman = time.time()
  tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
  anahtarkelime = "python sqlite3"
  deger =random.randrange(1,10)
  cursor.execute("INSERT INTO Tablo1 (ZAMAN,TARIH,ANAHTARKELIME,DEGER)VALUES (?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
  con.commit()
def degerekle(sayi=1):
   i = 0
   print(sayi)
   while (i < sayi):
       rastgeledegerekle()
       time.sleep(1)
       i += 1
def degeroku():
   cursor.execute("SELECT * FROM Tablo1 WHERE deger = 9.0")
   data = cursor.fetchall()
   print(type(data))
   j = 0
   for i in data:
       print(i )
def satirsil():
   cursor.execute("DELETE FROM Tablo1 WHERE ..")
tablooluştur()
degerekle(5)
degeroku()

con.close()

"""

sayi1 = 12
sayi2 = 0
print(sayi1/sayi2)