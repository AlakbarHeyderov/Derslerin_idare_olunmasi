class User:
    def __init__(self, _qrup, _ad, _soyad):
        self.qrup = _qrup
        self.ad = _ad
        self.soyad = _soyad

    def show(self):
        print(f"{self.qrup} nomreli qrupun telebesi {self.ad} {self.soyad} xos geldiniz.")

class yeniDictYarat(dict):
    def __init__(self):
        self = dict()
    def keyValueElaveEt(self,key,value):
        self[key]=value

