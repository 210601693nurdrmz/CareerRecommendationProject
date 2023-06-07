from Insan import Insan


class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube_ay = tecrube_ay
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube_ay(self):
        return self.__tecrube_ay

    def set_tecrube_ay(self, tecrube_ay):
        self.__tecrube_ay = tecrube_ay

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    # Zam hakkını hesaplayan metot
    def zam_hakki(self):
        tecrube_yil = self.get_tecrube_ay() // 12
        if tecrube_yil < 2:
            zam_orani = 0
        elif 2 <= tecrube_yil < 4:
            if self.get_maas() < 15000:
                zam_orani = (self.get_maas() * tecrube_yil) / 100
            else:
                zam_orani = 0
        else:
            if self.get_maas() < 25000:
                zam_orani = ((self.get_maas() * tecrube_yil) / 100) / 2
            else:
                zam_orani = 0
        yeni_maas = self.get_maas() + zam_orani
        if yeni_maas == self.get_maas():
            yeni_maas = yeni_maas
        return yeni_maas

    # İlgili yerlerde try/except kullanıyoruz
    def __str__(self):
        try:
            return super().__str__() + f"Tecrübe: {self.get_tecrube_ay()} ay\nYeni Maaş: {self.zam_hakki()} TL\n"
        except (TypeError, ValueError):
            return "Tecrübe veya maaş değeri geçersiz.\n"