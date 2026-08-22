import os


def gorevekle():
    t()
    x = 0
    gorev = input("Eklemek istediğiniz görev : ")
    with open("görevler.txt", "a", encoding="utf-8") as file:
        file.write(gorev + "\n")
    while True:
        devam = input("Devam etmek ister misin? (e/h) : ").lower().strip()
        if devam == "e":
            menu()
        elif devam == "h":
            exit()
        else:
            print("Geçersiz işlem.")


def gorevsil():
    t()
    silineceksatir = int(input("Silinecek görevin numarasını giriniz"))
    # SATIR SİLME FONKSİYONU EKLENECEK

    while True:
        devam = input("Devam etmek ister misin? (e/h) : ").lower().strip()
        if devam == "e":
            menu()
        elif devam == "h":
            exit()
        else:
            print("Geçersiz işlem.")


def gorevler():
    t()
    with open("görevler.txt", "r", encoding="utf-8") as file:
        result = file.read()
        print(result)

    while True:
        devam = input("Devam etmek ister misin? (e/h) : ").lower().strip()
        if devam == "e":
            menu()
        elif devam == "h":
            exit()
        else:
            print("Geçersiz işlem.")


def t():
    os.system("cls")


def menu():
    t()
    with open("görevler.txt", "r", encoding="utf-8") as file:
        sayi = len(file.readlines())
        sayi = str(sayi)
    while True:
        print(f""" 
        1 - Görev ekle   2 - Görev sil
        3 - Görevlerim   4 - Çıkış

        Güncel görev sayısı : {sayi}
        """)
        islem = input("Bir işlem seç : ").strip()
        if islem == "1":
            gorevekle()
        elif islem == "2":
            gorevsil()
        elif islem == "3":
            gorevler()
        elif islem == "4":
            exit()
        else:
            print("Geçersiz seçenek girdiniz.")


menu()
