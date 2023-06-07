import pandas as pd

from BeyazYaka import BeyazYaka
from Calisan import Calisan
from Insan import Insan
from Issiz import Issiz
from MaviYaka import MaviYaka

df = pd.DataFrame()
def insan_olustur():
    # Input değerlerini kontrol ediyoruz
    while True:
        try:
            tc_no = input('TC No: ')
            ad = input('Ad: ')
            soyad = input('Soyad: ')
            yas = int(input('Yaş: '))
            cinsiyet = input('Cinsiyet: ')
            uyruk = input('Uyruk: ')
            break
        except ValueError:
            print("Geçersiz değer. Lütfen tekrar giriniz.")

    insan = Insan(tc_no, ad, soyad, yas, cinsiyet, uyruk)

    # İnsan nesnesini bir veri çerçevesine dönüştürüyoruz
    insan_df = pd.DataFrame(vars(insan), index=[0])

    # Veri çerçevesini global olarak tanımladığımız df ile birleştiriyoruz
    global df
    df = pd.concat([df, insan_df], ignore_index=True)


def calisan_olustur():
    # Input değerlerini kontrol ediyoruz
    while True:
        try:
            tc_no = input('TC No: ')
            ad = input('Ad: ')
            soyad = input('Soyad: ')
            yas = int(input('Yaş: '))
            cinsiyet = input('Cinsiyet: ')
            uyruk = input('Uyruk: ')

            # Sektör seçimini kontrol ediyoruz
            while True:
                sektor = input('Sektör (teknoloji/muhasebe/inşaat/diğer): ')
                if sektor in ('teknoloji', 'muhasebe', 'inşaat', 'diğer'):
                    break
                else:
                    print("Geçersiz sektör. Lütfen tekrar giriniz.")

            tecrube_ay = int(input('Tecrübe (Ay): '))
            maas = int(input('Maaş: '))
            break
        except ValueError:
            print("Geçersiz değer. Lütfen tekrar giriniz.")

    calisan_tipi = input('Çalışan Tipi (Mavi Yaka/Beyaz Yaka): ')
    if calisan_tipi == 'Mavi Yaka':
        # Yıpranma payını kontrol ediyoruz
        while True:
            try:
                yipranma_payi = float(input('Yıpranma Payı: '))
                break
            except ValueError:
                print("Geçersiz yıpranma payı. Lütfen tekrar giriniz.")
        calisan = MaviYaka(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas, yipranma_payi)
    elif calisan_tipi == 'Beyaz Yaka':
        # Teşvik primini kontrol ediyoruz
        while True:
            try:
                tesvik_primi = int(input('Teşvik Primi: '))
                break
            except ValueError:
                print("Geçersiz teşvik primi. Lütfen tekrar giriniz.")
        calisan = BeyazYaka(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas, tesvik_primi)
    else:
        calisan = Calisan(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas)

    # Çalışan nesnesini bir veri çerçevesine dönüştürüyoruz
    calisan_df = pd.DataFrame(vars(calisan), index=[0])

    # Veri çerçevesini global olarak tanımladığımız df ile birleştiriyoruz
    global df
    df = pd.concat([df, calisan_df], ignore_index=True)


def issiz_olustur():
    # Input değerlerini kontrol ediyoruz
    while True:
        try:
            tc_no = input('TC No: ')
            ad = input('Ad: ')
            soyad = input('Soyad: ')
            yas = int(input('Yaş: '))
            cinsiyet = input('Cinsiyet: ')
            uyruk = input('Uyruk: ')

            mavi_yaka_tecrube = int(input('Mavi Yaka Tecrübesi (Yıl): '))
            beyaz_yaka_tecrube = int(input('Beyaz Yaka Tecrübesi (Yıl): '))
            yonetici_tecrube = int(input('Yönetici Tecrübesi (Yıl): '))
            break
        except ValueError:
            print("Geçersiz değer. Lütfen tekrar giriniz.")

    statu_tecrube = {
        'mavi yaka': mavi_yaka_tecrube,
        'beyaz yaka': beyaz_yaka_tecrube,
        'yonetici': yonetici_tecrube
    }
    issiz = Issiz(tc_no, ad, soyad, yas, cinsiyet, uyruk, statu_tecrube)

    # İşsiz nesnesini bir veri çerçevesine dönüştürüyoruz
    issiz_df = pd.DataFrame({"tc_no": tc_no,
                             "ad": ad,
                             "soyad": soyad,
                             "yas": yas,
                             "cinsiyet": cinsiyet,
                             "uyruk": uyruk,
                             "sektor": None,
                             "tecrube_ay": None,
                             "maas": None,
                             "calisan_tipi": None,
                             "yipranma_payi": None,
                             "tesvik_primi": None,
                             "statu_tecrube": statu_tecrube}, index=[0])

    # Veri çerçevesini global olarak tanımladığımız df ile birleştiriyoruz
    global df
    df = pd.concat([df, issiz_df], ignore_index=True)


# İnsan sınıfı için nesne üretiyoruz ve bilgileri yazdırıyoruz
print("İnsan sınıfı için 2 nesne üretiniz.")
for i in range(2):
    insan_olustur()
    print(df.iloc[-1])

# İşsiz sınıfı için nesne üretiyoruz ve bilgileri yazdırıyoruz
print("İşsiz sınıfı için 3 nesne üretiniz.")
for i in range(3):
    issiz_olustur()
    print(df.iloc[-1])

# Çalışan sınıfı için nesne üretiyoruz ve bilgileri yazdırıyoruz
print("Çalışan sınıfı için 3 nesne üretiniz.")
for i in range(3):
    calisan_olustur()
    print(df.iloc[-1])

# Mavi yaka sınıfı için nesne üretiyoruz ve bilgileri yazdırıyoruz
print("Mavi yaka sınıfı için 3 nesne üretiniz.")
for i in range(3):
    calisan_olustur()
    print(df.iloc[-1])

# Beyaz yaka sınıfı için nesne üretiyoruz ve bilgileri yazdırıyoruz
print("Beyaz yaka sınıfı için 3 nesne üretiniz.")
for i in range(3):
    calisan_olustur()
    print(df.iloc[-1])

# a) Bazı değişken değerleri diğer nesneler için boş olabilir, DataFrame için bu değerleri 0 atayınız.
df = df.fillna(0)

# b) Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş ortalamalarını her grup için hesaplayınız ve yazdırınız.
grup = df.groupby("calisan_tipi")
# c) Maaşı 15000TL üzerinde olanların toplam sayısını bulunuz.
sayi = (df["maas"] > 15000).sum()
print(sayi)

# d) Yeni maaşa göre DataFrame’i küçükten büyüğe sıralayınız ve yazdırınız.
df = df.sort_values(by="maas")
print(df)

# e) Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulunuz ve yazdırınız.
beyaz_yaka = df[(df["calisan_tipi"] == "Beyaz Yaka") & (df["tecrube_ay"] > 36)]
print(beyaz_yaka)

# f) Yeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanları, tc_no ve yeni_maaş sütunlarını seçerek gösteriniz ve yazdırınız.
secim = df[(df["maas"] > 10000)].iloc[1:5][["tc_no", "maas"]]
print(secim)

# g) Var olan DataFrame’den ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame elde ediniz ve yazdırınız.
yeni_df = df[["ad", "soyad", "sektor", "maas"]]
print(yeni_df)
