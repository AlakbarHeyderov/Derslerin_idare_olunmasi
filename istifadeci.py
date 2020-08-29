from clases import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Melumatlari Dict kimi hazirlamaq~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def istfadeceElavesi(_group, _name, _surname):
    creatDict = yeniDictYarat()
    creatDict.keyValueElaveEt("Grup", _group)
    creatDict.keyValueElaveEt("Ad", _name)
    creatDict.keyValueElaveEt("Soyad", _surname)
    return creatDict
