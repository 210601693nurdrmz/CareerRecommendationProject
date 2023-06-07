from Insan import Insan


class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statu_tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statu_tecrube = statu_tecrube
        # En uygun statüyü hesaplayıp bir public değişkene atıyoruz
        self.statu = self.statu_bul()

    def get_statu_tecrube(self):
        return self.__statu_tecrube

    def set_statu_tecrube(self, statu_tecrube):
        self.__statu_tecrube = statu_tecrube

    # En uygun statüyü hesaplayan metot
    def statu_bul(self):
        # Statü tecrübesi dictionary'sini alıyoruz
        tecrube_dict = self.get_statu_tecrube()

        # Statülerin etki oranlarını bir dictionary'de tutuyoruz
        etki_dict = {
            "mavi yaka": 0.2,
            "beyaz yaka": 0.35,
            "yonetici": 0.45
        }

        # Statülerin puanlarını hesaplamak için boş bir dictionary oluşturuyoruz
        puan_dict = {}

        # Her statü için puanı hesaplayıp dictionary'e ekliyoruz
        for statu in tecrube_dict:
            puan_dict[statu] = tecrube_dict[statu] * etki_dict[statu]

        # Puanları büyükten küçüğe sıralayıp en büyük puanlı olanın statüsünü döndürüyoruz
        puan_listesi = sorted(puan_dict.items(), key=lambda x: x[1], reverse=True)

        return puan_listesi[0][0]

    # İlgili yerlerde try/except kullanıyoruz
    def __str__(self):
        try:
            return super().__str__() + f"Statü: {self.statu}\n"
        except AttributeError:
            return "Statü bulunamadı.\n"
