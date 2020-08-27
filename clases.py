class User:
    def __init__(self, _qrup, _ad, _soyad):
        self.qrup = _qrup
        self.ad = _ad
        self.soyad = _soyad

    def show(self):
        print(f"{self.qrup} nomreli qrupun telebesi {self.ad} {self.soyad} xos geldiniz.")

# class Json:
#     def show(self):
#         daxil_olanlari_qeyd_et=open("json_istifadeci_bazasi.json","a")
#         json_data = {"istifadeciler":[
#                 {
#                     "group": self.qrup,
#                     "name": self.ad,
#                     "surname": self.soyad
#                 }
#             ]}
#         daxil_olanlari_qeyd_et.write(json.dumps(json_data))
