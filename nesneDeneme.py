import random
import sqlite3


class Asker:
    def __init__(self, p_isim="Er", p_hp=1000, p_ap=100, p_mp=10):
        self.isim = p_isim
        self.hp = p_hp
        self.ap = p_ap
        self.mp = p_mp

    def saldir(self, defans):
        print(self.isim, ", ", defans.isim, "'e saldırıyor...")
        defans.hp = defans.hp - self.ap
        self.mp -= 1
        print("Atak başarılı. {} için kalan can : {}".format(defans.isim, defans.hp))

    def printS(self):
        print("İsim:{}, Hp:{}, Ap:{}, Mp:{}".format(self.isim, self.hp, self.ap, self.mp))

    def oldumu(self):
        if(self.hp<=0):
            return True
        return False

    def mpvarmi(self):
        if(self.mp>0):
            return True
        return False

class Boluk:
    boluk = []
    def __init__(self, isim, sayi):
        self.isim = isim
        self.kapasite = sayi
        i = 1
        while (i <= sayi):
            yeniasker = Asker("Asker" + str(i), random.randrange(1000, 3000), random.randrange(100, 500),
                              random.randrange(5, 30))
            self.boluk.append(yeniasker)
            i += 1

    def printList(self):
        for i in self.boluk:
            i.printS()

    def hucum(self, dusman, atak):
        if(atak == 1):
            askersec = random.choice(self.boluk)
            if(askersec.mpvarmi()):
                askersec.saldir(dusman)
                if(dusman.oldumu()):
                    print("******* Savaş sonlandı. Kazanan: {} *******".format(self.isim))
                    return False
            else:
                print("Atak başarısız. Yetersiz mp")
        else:
            askersec = random.choice(self.boluk)
            if (dusman.mpvarmi()):
                dusman.saldir(askersec)
                if (askersec.oldumu()):
                    print("Dikkat: {} öldü.".format(askersec.isim))
                    self.boluk.remove(askersec)
            else:
                print("Atak başarısız. Yetersiz mp")
                dusman.mp += 1
        return True
    def yasayanvarmi(self):
        if(len(self.boluk)>0):
            return True
        print("******* Savaş sonlandı. Kazanan: Düşman ********")
        return False

bolukad = input("Bölük adı giriniz.")
askersay = int(input("Asker sayısı giriniz."))
# bölük adı veritabanında kayıtlı ise hata ver
print("-------Savaş başlıyor-------")
boluk = Boluk(bolukad,askersay)
boluk.printList()
dusman = Asker("Düşman", 10000, 900, 1000)
dusman.printS()

tur = 1
a = True
b = True
while (a and b):
    print("----- {}. Tur  ----------".format(tur))
    tur += 1
    a = boluk.hucum(dusman,1)
    boluk.hucum(dusman,2)
    b = boluk.yasayanvarmi()

# tablolardaki her bir veriye unique anahtar vermek
# her bir değişiklik yapıldıkça tabloya kayıt etmek
#
con = sqlite3.connect("nesneDeneme.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS BOLUK (KEY TEXT, ISIM TEXT, KAPASITE INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS ASKERLER(KEY TEXT, ISIM TEXT, HP INT, AP INT, MP INT, HAYATTAMI TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS SAVASLAR(KEY TEXT, NUMARA INT, KATILIMCISAYISI INT, KAZANAN TEXT, TARIH DATE)")
cursor.execute("CREATE TABLE IF NOT EXISTS HUCUMLAR(KEY TEXT, SALDIRAN TEXT, SAVUNAN TEXT, VERILENZARAR INT, TARIH DATE)")


con.commit()