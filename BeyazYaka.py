from Calisan import Calisan


class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    # Zam hakkını hesaplayan metot
    def zam_hakki(self):
        tecrube_yil = self.get_tecrube_ay() // 12
        if tecrube_yil < 2:
            zam_miktari = self.get_tesvik_primi()
        elif 2 <= tecrube_yil < 4:
            if self.get_maas() < 15000:
                zam_miktari = ((self.get_maas() * tecrube_yil) / 100) * 5 + self.get_tesvik_primi()
            else:
                zam_miktari = 0
        else:
            if self.get_maas() < 25000:
                zam_miktari = ((self.get_maas() * tecrube_yil) / 100) * 4 + self.get_tesvik_primi()
            else:
                zam_miktari = 0
        yeni_maas = self.get_maas() + zam_miktari
        if yeni_maas == self.get_maas():
            yeni_maas = yeni_maas
        return yeni_maas

    # İlgili yerlerde try/except kullanıyoruz
    def __str__(self):
        try:
            return super().__str__() + f"Teşvik Primi: {self.get_tesvik_primi()} TL\n"
        except (TypeError, ValueError):
            return "Teşvik primi değeri geçersiz.\n"
