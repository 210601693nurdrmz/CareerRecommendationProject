from Calisan import Calisan


class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        tecrube_yil = self.get_tecrube_ay() // 12
        if tecrube_yil < 2:
            zam_orani = self.get_yipranma_payi() * 10
        elif 2 <= tecrube_yil < 4:
            if self.get_maas() < 15000:
                zam_orani = ((self.get_maas() * tecrube_yil) / 100) / 2 + (self.get_yipranma_payi() * 10)
            else:
                zam_orani = 0
        else:
            if self.get_maas() < 25000:
                zam_orani = ((self.get_maas() * tecrube_yil) / 100) / 3 + (self.get_yipranma_payi() * 10)
            else:
                zam_orani = 0
        yeni_maas = self.get_maas() + zam_orani
        if yeni_maas == self.get_maas():
            yeni_maas = yeni_maas
        return yeni_maas
