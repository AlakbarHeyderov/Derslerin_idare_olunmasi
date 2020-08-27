import webbrowser
import json
from clases import User

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


def start():
    qrup = input("Qrup adini yazin: ")
    ad = input("Adinizi qeyd edin: ")
    soyad = input("Soyadinizi qeyd edin: ")
    daxil_olanlari_qeyd_et=open("json_istifadeci_bazasi.json","a")
    json_data = {"istifadeciler":[
                   {
                       "group": qrup,
                       "name": ad,
                       "surname": soyad
                   }
               ]}
    daxil_olanlari_qeyd_et.write(json.dumps(json_data))
    User(qrup, ad, soyad).show()
    daxil_olanlari_qeyd_et.close()
    print()
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
            print("Dersin progrmina baxmaq ucun 1 e. \n"
                  "dersin recorduna baxmaq ucun 2 ye \n"
                  "dersde yazilan kodlari gozden kecirmek ucun 3 e basin.")
            week6_day1()
        elif hansi_gun == "day-2":
            print("Dersin progrmina baxmaq ucun 1 e. \n"
                  "dersin recorduna baxmaq ucun 2 ye \n"
                  "dersde yazilan kodlari gozden kecirmek ucun 3 e basin.")
            week6_day2()
        elif hansi_gun == "day-3":
            print("Dersin progrmina baxmaq ucun 1 e. \n"
                  "dersin recorduna baxmaq ucun 2 ye \n"
                  "dersde yazilan kodlari gozden kecirmek ucun 3 e basin.")
            week6_day3()
        elif hansi_gun == "day-4":
            print("Dersin progrmina baxmaq ucun 1 e. \n"
                  "dersin recorduna baxmaq ucun 2 ye \n"
                  "dersde yazilan kodlari gozden kecirmek ucun 3 e basin.")
            week6_day4()
        elif hansi_gun == "day-5":
            print("Dersin progrmina baxmaq ucun 1 e. \n"
                  "dersin recorduna baxmaq ucun 2 ye \n"
                  "dersde yazilan kodlari gozden kecirmek ucun 3 e basin.")
            week6_day5()
        else:
            print("zehmet olmasa duzgun secim edin")
            hefteye_secimi()

    else:
        print("xeta")
        hefteye_secimi()


def week6_day1():
    emr_secilmesi = input("Secdiyiniz emri qeyd edin: ")
    if emr_secilmesi == "1":
        webbrowser.get(chrome_path).open(
            'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp')
        print("programin islemeyine davam etmek isteyirsen? Beli/Xeyir  emri ile cavablayin")
        islemeye_davam = input("Cavabiniz: ")
        if islemeye_davam == "Beli":
            hefteye_secimi()
        elif islemeye_davam == "Xeyir":
            print("Ugurlar!")
        else:
            print("Yanlis kod daxil etdiniz.")
            hefteye_secimi()
    # else:
    #     week6_day1()
    elif emr_secilmesi == "2":
        webbrowser.get(chrome_path).open(
            "https://drive.google.com/file/d/18fVXXQyGrVZMBa5DojiSa7JjPSq2dgFK/view?usp=sharing")
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
        webbrowser.get(chrome_path).open("https://drive.google.com/drive/u/0/folders/1VTVFT_GGfW94dbc65Cv4iaVM4CffPKhe")
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


def week6_day2():
    emr_secilmesi = input("Secdiyiniz emri qeyd edin: ")
    if emr_secilmesi == "1":
        webbrowser.get(chrome_path).open(
            'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp')
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
        webbrowser.get(chrome_path).open(
            "https://drive.google.com/file/d/1fdv5z1vKNbG5dEbWRu-DrjhwaOPOuuM9/view?usp=sharing")
        iprint("programin islemeyine davam etmek isteyirsen? Beli/Xeyir  emri ile cavablayin")
        islemeye_davam = input("Cavabiniz: ")
        if islemeye_davam == "Beli":
            hefteye_secimi()
        elif islemeye_davam == "Xeyir":
            print("Ugurlar!")
        else:
            print("Yanlis kod daxil etdiniz.")
            hefteye_secimi()
    elif emr_secilmesi == "3":
        webbrowser.get(chrome_path).open("https://drive.google.com/drive/u/0/folders/1YqFwGUGzabdcw_w7ZEw6bUVe9o8fQvg3")
    else:
        print("Xeta")
        week6_day2()


def week6_day3():
    emr_secilmesi = input("Secdiyiniz emri qeyd edin: ")
    if emr_secilmesi == "1":
        webbrowser.get(chrome_path).open(
            'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp')
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
        webbrowser.get(chrome_path).open(
            "https://drive.google.com/file/d/1xXjRSTpVa4jpO7ipDuxB3Rs1kmmx-V7d/view?usp=sharing")
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
        webbrowser.get(chrome_path).open("https://drive.google.com/drive/u/0/folders/1aM1Mf2LjR0ElRM0r6oGKf97wcaK-BHHw")
    else:
        print("xeta")
        week6_day3()


def week6_day4():
    emr_secilmesi = input("Secdiyiniz emri qeyd edin: ")
    if emr_secilmesi == "1":
        webbrowser.get(chrome_path).open(
            'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp')
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
        webbrowser.get(chrome_path).open(
            "https://drive.google.com/file/d/1IzcrTRJ9imJO-jAoSndanQZGF-2_Ik94/view?usp=sharing")
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
        webbrowser.get(chrome_path).open("https://drive.google.com/drive/u/0/folders/1I6mbMrcKRCiqamPXeZrg7YTdvYlvebz9")
    else:
        print("xeta")
        week6_day4()


def week6_day5():
    emr_secilmesi = input("Secdiyiniz emri qeyd edin: ")
    if emr_secilmesi == "1":
        webbrowser.get(chrome_path).open(
            'https://docs.google.com/document/d/1xWE_32xpUsuf0E5IP3jmbl0VuCK0BKbcfc1iK4jl-bk/edit#heading=h.t2d024q8l2bp')
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
        # webbrowser.get(chrome_path).open(
        #     "https://drive.google.com/file/d/1IzcrTRJ9imJO-jAoSndanQZGF-2_Ik94/view?usp=sharing")
        print("Video heleki teyin olunmayib!")
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
        # webbrowser.get(chrome_path).open("https://drive.google.com/drive/u/0/folders/1I6mbMrcKRCiqamPXeZrg7YTdvYlvebz9")
        print("Ders programi heleki teyin olunmayib!")
    else:
        print("xeta")
        week6_day5()


start()
