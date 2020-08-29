import webbrowser
import json
from clases import User
from clases import yeniDictYarat
from istifadeci import *
from vareble import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Programin strat hissesi~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def start():
    daxil_olanlari_qeyd_et = open("testjsonfile.json", "a")
    json_data = yeniDictYarat()
    json_data.keyValueElaveEt("Telebeler", [])
    istfadeceElavesi(qrup, ad, soyad)
    json_data["Telebeler"].append(istfadeceElavesi(qrup, ad, soyad))
    daxil_olanlari_qeyd_et.write(json.dumps(json_data))
    User(qrup, ad, soyad).show()
    daxil_olanlari_qeyd_et.close()
    print("Bu program derslerin duzgun wekilde \n"
          "idare olunmai ucun tertib edilib.\n"
          "Zehmet olmasa dersin heftesini ve \n"
          "gununu secin")
    print("Program 6 ci heftenden sonraki merhele"
          "ucun nezerde tutulub")

    hefteye_secimi()


def hefteye_secimi():
    hansi_hefte = input("Hefteni 'week-1' formatinda qeyd edin: ")
    if hansi_hefte == "week-6":
        hansi_gun = input("Heftenin gununu 'day-1' formatinda qeyd edin: ")
        if hansi_gun == "day-1":
            print(ders_secimi)
            week6_day1()
        elif hansi_gun == "day-2":
            print(ders_secimi)
            week6_day2()
        elif hansi_gun == "day-3":
            print(ders_secimi)
            week6_day3()
        elif hansi_gun == "day-4":
            print(ders_secimi)
            week6_day4()
        elif hansi_gun == "day-5":
            print(ders_secimi)
            week6_day5()
        else:
            print("Zehmet olmasa duzgun secim edin")
            hefteye_secimi()

    else:
        print("xeta")
        hefteye_secimi()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Heftenin Gunlerini Creat elemek ucun~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def creatWekk(_record, _program, _dersde_yazilan):
    emr_secilmesi = input("Secdiyiniz emri qeyd edin: ")

    if emr_secilmesi == "1":
        webbrowser.get(chrome_path).open(_program)
        print("programin islemeyine davam etmek isteyirsen? Beli/Xeyir  emri ile cavablayin")
        islemeye_davam = input("Cavabiniz: ")
        if islemeye_davam == "Beli":
            hefteye_secimi()
        elif islemeye_davam == "Xeyir":
            print("Ugurlar!")
        else:
            print("Yanlis kod daxil etdiniz.")
            hefteye_secimi()
    elif emr_secilmesi == "2":
        webbrowser.get(chrome_path).open(_record)
        print("programin islemeyine davam etmek isteyirsen? Beli/Xeyir  emri ile cavablayin")
        islemeye_davam = input("Cavabiniz: ")
        if islemeye_davam == "Beli":
            hefteye_secimi()
        elif islemeye_davam == "Xeyir":
            print("Ugurlar!")
        else:
            print("Yanlis kod daxil etdiniz.")
            hefteye_secimi()
    elif emr_secilmesi == "3":
        webbrowser.get(chrome_path).open(_dersde_yazilan)
        print("programin islemeyine davam etmek isteyirsen? Beli/Xeyir  emri ile cavablayin")
        islemeye_davam = input("Cavabiniz: ")
        if islemeye_davam == "Beli":
            hefteye_secimi()
        elif islemeye_davam == "Xeyir":
            print("Ugurlar!")
        else:
            print("Yanlis kod daxil etdiniz.")
            hefteye_secimi()
    else:
        print("Xeta")
        week6_day1()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Hefteler~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def week6_day1():
    week6_day1_rec = 'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp'
    week6_day1_program = "https://drive.google.com/file/d/18fVXXQyGrVZMBa5DojiSa7JjPSq2dgFK/view?usp=sharing"
    week6_day1_dersde_yazilan = "https://drive.google.com/drive/u/0/folders/1VTVFT_GGfW94dbc65Cv4iaVM4CffPKhe"
    creatWekk(week6_day1_rec, week6_day1_program, week6_day1_dersde_yazilan)


def week6_day2():
    week6_day2_rec = 'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp'
    week6_day2_program = "https://drive.google.com/file/d/1fdv5z1vKNbG5dEbWRu-DrjhwaOPOuuM9/view?usp=sharing"
    week6_day2_dersde_yazilan = "https://drive.google.com/drive/u/0/folders/1YqFwGUGzabdcw_w7ZEw6bUVe9o8fQvg3"
    creatWekk(week6_day2_rec, week6_day2_program, week6_day2_dersde_yazilan)


def week6_day3():
    week6_day3_rec = 'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp'
    week6_day3_program = "https://drive.google.com/file/d/1xXjRSTpVa4jpO7ipDuxB3Rs1kmmx-V7d/view?usp=sharing"
    week6_day3_dersde_yazilan = "https://drive.google.com/drive/u/0/folders/1aM1Mf2LjR0ElRM0r6oGKf97wcaK-BHHw"
    creatWekk(week6_day3_rec, week6_day3_program, week6_day3_dersde_yazilan)


def week6_day4():
    week6_day4_rec = 'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp'
    week6_day4_program = "https://drive.google.com/file/d/1IzcrTRJ9imJO-jAoSndanQZGF-2_Ik94/view?usp=sharing"
    week6_day4_dersde_yazilan = "https://drive.google.com/drive/u/0/folders/1I6mbMrcKRCiqamPXeZrg7YTdvYlvebz9"
    creatWekk(week6_day4_rec, week6_day4_program, week6_day4_dersde_yazilan)


def week6_day5():
    week6_day5_rec = 'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp'
    week6_day5_program = "https://drive.google.com/file/d/1IzcrTRJ9imJO-jAoSndanQZGF-2_Ik94/view?usp=sharing"
    week6_day5_dersde_yazilan = "https://drive.google.com/drive/u/0/folders/1I6mbMrcKRCiqamPXeZrg7YTdvYlvebz9"
    creatWekk(week6_day5_rec, week6_day5_program, week6_day5_dersde_yazilan)


start()
