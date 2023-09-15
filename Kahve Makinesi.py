import time

kahve_listesi = {
    "FILTRE KAHVE": 10.,
    "AMERICANO": 14.,
    "LATTE": 15.,
    "FLAT WHITE": 18.,
    "EKSTRA SHOT": 9.
}


# Kahve otomatı sınıfı oluşturulacak.
class Makine():
    # __init__ fonkisyonu ile parametreleri belirleme otomat_durum, kahve_listesi, seker_miktari, default_kahve_miktarı.
    def __init__(self, otomat_durum="Kapalı", seker_miktari=0, default_kahve_miktarı=1):
        self.otomat_durum = otomat_durum
        self.default_kahve_miktarı = default_kahve_miktarı
        self.seker_miktari = seker_miktari
        # otomat_ac isimli bir fonksiyon oluşturup self parametresi ekleyelim. ö

    def otomatAc(self):
        if (self.otomat_durum == "Açık"):
            # otomat_durum açıksa kahve makinası zaten açık yazdıralım. ö
            print("Otomat zaten açık.")

        else:
            # Diğer durumlarda ekrana Otomat Açılıyor yazdıralım ve otomat_durum açık hale getirelim. ö
            print("Otomat açılıyor...")
            self.otomat_durum = "Açık"
            print("Otomat açıldı.")

        # otomat_kapat isimli bir fonksiyon oluşturup self parametresi ekleyelim. devamı aynı ö

    def otomatKapa(self):
        if self.otomat_durum == "Kapalı":
            print("Otomat zaten kapalı.")
        else:
            print("Otomat kapatılıyor...")
            self.otomat_durum = "Kapalı"
            print("Otomat kapatıldı.")

        # şeker_ayarı isimli bir fonksiyon oluşturup self parametresi ekleyelim. b

    def seker_ayarı(self):
        if (self.otomat_durum == "Açık"):
            print("*" * 40)
            while True:
                print("-" * 40)
                secim = input(
                    f"Şeker miktarınız {self.seker_miktari}. Arttırmak için +,\nazaltmak için ise - tuşlarını kullanınız. \nÇıkış yapmak için + veya - dışında herhangi bir tuşa basmanız yeterlidir.")
                if (secim == "-"):
                    if (self.seker_miktari == 0):
                        print("Şeker zaten sıfır!")
                    else:
                        self.seker_miktari -= 1
                        print(f"Şeker miktarınız {self.seker_miktari} olarak güncellendi.")
                elif (secim == "+"):
                    # Şeker miktarı en çok 5'e kadar arttırılabilir.
                    if (self.seker_miktari != 5):
                        self.seker_miktari += 1
                        print(f"Şeker miktarınız {self.seker_miktari} olarak güncellendi.")
                    else:
                        print("Şeker miktarınız maksimum 5 olabilir.")
                else:
                    print("Çıkış yapılıyor.")
                    break
        else:
            print("Kahve makinesi kapalı. Lütfen kahve makinesini açınız.")

        # ekstrakahve_ayarı isimli bir fonksiyon oluşturup self parametresi ekleyelim.b

    def extra_kahve_ayarı(self):
        if (self.otomat_durum == "Açık"):
            print("*" * 40)
            while True:
                print("-" * 40)
                extra_kahve_miktarı = int(input(
                    "İçeceğinizdeki kahve oranını arttırmak isterseniz, \nkaç shot ekstra kahve istediğinizi sayı olarak giriniz. \nEkstra kahve istemiyorsanız 0'a basınız."))
                if (extra_kahve_miktarı > 3):
                    print("Extra kahve miktarı en fazla üç shot olabilir. ")
                    self.default_kahve_miktarı += 3
                    print(f"Kahve miktarınız {self.default_kahve_miktarı} olarak güncellendi.")
                    break
                elif (extra_kahve_miktarı > 0):
                    self.default_kahve_miktarı += extra_kahve_miktarı
                    print(f"Kahve miktarınız {self.default_kahve_miktarı} olarak güncellendi.")
                    break
                else:
                    print("Ekstra kahve miktarı - olarak seçilemez.")
                    print("Çıkış yapılıyor.")
                    break
        else:
            print("Kahve makinesi kapalı. Lütfen kahve makinesini açınız.")

        # menü gösterme yazılmalı. Ekstradan yazdım sanırım.

    def display_menu(self):
        if (self.otomat_durum == "Açık"):
            print("-----Kahve Menüsü-----")
            for kahve in list(kahve_listesi.keys()):
                print(f"{kahve.upper():<20} : {kahve_listesi[kahve]} TL")
        else:
            print("Kahve makinesi kapalı. Lütfen kahve makinesini açınız.")

        # kahve_ekle isimli bir fonksiyon oluşturup self ve kanal_ismi parametresi gönderelim. c default_data.update({'item3': 3})

    def kahve_ekle(self, kahve_isim, kahve_fiyatı):
        if (self.otomat_durum == "Açık"):
            print("Kahve Ekleniyor...")
            time.sleep(1)
            self.kahve_listesi.update({kahve_isim: kahve_fiyatı})
            print("Kahve Eklendi...")
        else:
            print("Kahve makinesi kapalı. Lütfen kahve makinesini açınız.")

        # Fiyat Değiştirme

    def fiyatDegis(self):
        if (self.otomat_durum == "Açık"):
            # Hangi kahvenin fiyatının değişeceğinin belirlenmesi
            degisecekKahve = input("Değiştirmek istediğiniz kahve: ")
            degisecekKahve = degisecekKahve.upper()
            # Yeni fiyatın belirlenmesi
            yeniFiyat = float(input("Yeni fiyat: "))
            # Dictionary yapısında alınan inputlara göre fiyat value'sının değiştirilmesi
            kahve_listesi[degisecekKahve] = yeniFiyat
            # Kullanıcıya başarılı olduğunun geri bildirimi
            print("Fiyat değiştirildi.")
        else:
            print("Kahve makinesi kapalı. Lütfen kahve makinesini açınız.")


makine = Makine()

# Ana fonksiyon
print("""
1.Otomatı Açma 
2.Otomatı Kapatma 
3.Menüyü gör 
4.Kahve Ekle
5.Fiyat Güncelleme 
6.Şeker Miktarı Ayarlama
7.Kahve Miktarı Ayarlama
8.Kahve Makinesi Bilgileri
Çıkmak için 'q' ya basın.
""")

#  While döngüsü kuralım. c

while True:
    print("*" * 40)
    islem = input("Yapmak istediğiniz işlemi seçiniz:")
    if (islem == "q"):
        print("İşleminiz sonlandırılıyor... ")
        break
    elif (islem == "1"):
        makine.otomatAc()
    elif (islem == "2"):
        makine.otomatKapa()
    elif (islem == "3"):
        makine.display_menu()
        # makine.menuGor()
    elif (islem == "4"):
        kahve_isimleri = input("Eklemek istediğiniz kahve isimini yazınız:")
        kahve_fiyatı = float(input("Eklediğiniz kahvenin fiyatını yazınız:"))
        kahve_listesi.update({kahve_isimleri: kahve_fiyatı})
        makine.display_menu()
    elif (islem == "5"):
        makine.fiyatDegis()
    elif (islem == "6"):
        makine.seker_ayarı()
    elif (islem == "7"):
        makine.extra_kahve_ayarı()
    elif (islem == "8"):
        print("Makine markası 'KafeinYet' dir... \nİyi günler dileriz.")

    else:
        print("İşleminiz geçersiz!")