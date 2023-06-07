class Insan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        # TC kimlik numarasını kontrol ediyoruz
        while True:
            try:
                tc_no = int(tc_no) # Sayı olup olmadığını kontrol ediyoruz
                if len(str(tc_no)) == 11: # 11 haneli olup olmadığını kontrol ediyoruz
                    self.__tc_no = tc_no
                    break
                else:
                    print("TC kimlik numarası 11 haneli olmalıdır.")
                    tc_no = input('TC No: ') # Yeniden girilmesini istiyoruz
            except ValueError:
                print("TC kimlik numarası sayı olmalıdır.")
                tc_no = input('TC No: ') # Yeniden girilmesini istiyoruz

        self.__ad = ad
        self.__soyad = soyad

        # Yaş değerini kontrol ediyoruz
        while True:
            try:
                yas = int(yas) # Tam sayı olup olmadığını kontrol ediyoruz
                self.__yas = yas
                break
            except ValueError:
                print("Yaş değeri tam sayı olmalıdır.")
                yas = input('Yaş: ') # Yeniden girilmesini istiyoruz

        # Cinsiyet değerini kontrol ediyoruz
        while True:
            if cinsiyet in ('Erkek', 'Kadın'): # Erkek ya da Kadın olup olmadığını kontrol ediyoruz
                self.__cinsiyet = cinsiyet
                break
            else:
                print("Cinsiyet değeri Erkek ya da Kadın olmalıdır.")
                cinsiyet = input('Cinsiyet: ') # Yeniden girilmesini istiyoruz

        # Uyruk değerini kontrol ediyoruz
        while True:
            if uyruk.isalpha(): # Harf olup olmadığını kontrol ediyoruz
                self.__uyruk = uyruk
                break
            else:
                print("Uyruk değeri bir ülke ismi olmalıdır.")
                uyruk = input('Uyruk: ') # Yeniden girilmesini istiyoruz


    def get_tc_no(self):
        return self.__tc_no

    def set_tc_no(self, tc_no):
        self.__tc_no = tc_no

    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_yas(self):
        return self.__yas

    def set_yas(self, yas):
        self.__yas = yas

    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    def get_uyruk(self):
        return self.__uyruk

    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\n"