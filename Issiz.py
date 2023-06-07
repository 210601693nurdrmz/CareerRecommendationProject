from Insan import Insan


class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statu_tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statu_tecrube = statu_tecrube
        self.__en_uygun_statu = self.statu_bul()

    def get_statu_tecrube(self):
        return self.__statu_tecrube

    def set_statu_tecrube(self, statu_tecrube):
        self.__statu_tecrube = statu_tecrube

    def get_en_uygun_statu(self):
        return self.__en_uygun_statu

    def statu_bul(self):
        mavi_yaka_puan = self.__statu_tecrube.get('mavi yaka', 0) * 0.2
        beyaz_yaka_puan = self.__statu_tecrube.get('beyaz yaka', 0) * 0.35
        yonetici_puan = self.__statu_tecrube.get('yonetici', 0) * 0.45
        max_puan = max(mavi_yaka_puan, beyaz_yaka_puan, yonetici_puan)
        if max_puan == mavi_yaka_puan:
            return 'mavi yaka'
        elif max_puan == beyaz_yaka_puan:
            return 'beyaz yaka'
        else:
            return 'yonetici'

    def __str__(self):
        return super().__str__() + f' En Uygun Statü: {self.get_en_uygun_statu()}'