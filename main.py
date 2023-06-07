import pandas as pd

from BeyazYaka import BeyazYaka
from Calisan import Calisan
from Issiz import Issiz
from MaviYaka import MaviYaka


def calisan_olustur():
    tc_no = input('TC No: ')
    ad = input('Ad: ')
    soyad = input('Soyad: ')
    yas = int(input('Yaş: '))
    cinsiyet = input('Cinsiyet: ')
    uyruk = input('Uyruk: ')
    sektor = input('Sektör: ')
    tecrube_ay = int(input('Tecrübe (Ay): '))
    maas = int(input('Maaş: '))

    calisan_tipi = input('Çalışan Tipi (Mavi Yaka/Beyaz Yaka): ')
    if calisan_tipi == 'Mavi Yaka':
        yipranma_payi = float(input('Yıpranma Payı: '))
        calisan = MaviYaka(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas, yipranma_payi)
    elif calisan_tipi == 'Beyaz Yaka':
        tesvik_primi = int(input('Teşvik Primi: '))
        calisan = BeyazYaka(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas, tesvik_primi)
    else:
        calisan = Calisan(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas)

    # Çalışan nesnesini bir veri çerçevesine dönüştürüyoruz
    calisan_df = pd.DataFrame(vars(calisan), index=[0])
    print(calisan_df)

def issiz_olustur():
    tc_no = input('TC No: ')
    ad = input('Ad: ')
    soyad = input('Soyad: ')
    yas = int(input('Yaş: '))
    cinsiyet = input('Cinsiyet: ')
    uyruk = input('Uyruk: ')

    mavi_yaka_tecrube = int(input('Mavi Yaka Tecrübesi (Yıl): '))
    beyaz_yaka_tecrube = int(input('Beyaz Yaka Tecrübesi (Yıl): '))
    yonetici_tecrube = int(input('Yönetici Tecrübesi (Yıl): '))
#değişiklikleri kaydetme testi
    statu_tecrube = {
        'mavi yaka': mavi_yaka_tecrube,
        'beyaz yaka': beyaz_yaka_tecrube,
        'yonetici': yonetici_tecrube
    }
    issiz = Issiz(tc_no, ad, soyad, yas, cinsiyet, uyruk, statu_tecrube)

    # İşsiz nesnesini bir veri çerçevesine dönüştürüyoruz
    issiz_df = pd.DataFrame(vars(issiz), index=[0])
    print(issiz_df)


while True:
    calisma_durumu = input('Çalışma Durumu (Çalışan/İşsiz/Çıkış): ')

    if calisma_durumu == 'Çalışan':
        calisan_olustur()
    elif calisma_durumu == 'İşsiz':
        issiz_olustur()
    elif calisma_durumu == 'Çıkış':
        break