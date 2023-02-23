#input
angka1 = int(input("Masukkan bilangan 1 : "))
angka2 = int(input("Masukkan bilangan 2 : "))
angka3 = int(input("Masukkan bilangan 3 : "))
angka4 = int(input("Masukkan bilangan 4 : "))
angka5 = int(input("Masukkan bilangan 5 : "))

#if dan else
if (angka1 < angka2 and angka1 > angka3 and angka1 > angka4 and angka1 < angka5) or (angka1 > angka2 and angka1 < angka3 and angka1 > angka4 and angka1 > angka5) or (angka1 > angka2 and angka1 > angka3 and angka1 < angka4 and angka1 > angka5) or (angka1 > angka2 and angka1 > angka3 and angka1 > angka4 and angka1 < angka5):
    print("Angka terbesar kedua :", angka1)
elif (angka2 < angka1 and angka2 > angka3 and angka2 > angka4 and angka2 > angka5) or (angka2 > angka1 and angka2 < angka3 and angka2 > angka4 and angka2 > angka5) or (angka2 > angka1 and angka2 > angka3 and angka2 < angka4 and angka2 > angka5) or (angka2 > angka1 and angka2 > angka3 and angka2 > angka4 and angka2 < angka5) :
    print("Angka terbesar kedua :", angka2)
elif (angka3 < angka2 and angka3 > angka1 and angka3 > angka4 and angka3 > angka5) or (angka3 > angka2 and angka3 < angka1 and angka3 > angka4 and angka3 > angka5) or (angka3 > angka2 and angka3 > angka1 and angka3 < angka4 and angka3 > angka5) or (angka3 > angka2 and angka3 > angka1 and angka3 > angka4 and angka3 < angka5) :
    print("Angka terbesar kedua :", angka3)
elif (angka4 < angka2 and angka4 > angka3 and angka4 > angka1 and angka4 > angka5) or (angka4 > angka2 and angka4 < angka3 and angka4 > angka1 and angka4 > angka5) or (angka4 > angka2 and angka4 > angka3 and angka4 < angka1 and angka4 > angka5) or (angka4 > angka2 and angka4 > angka3 and angka4 > angka1 and angka4 < angka5) :
    print("Angka terbesar kedua :", angka4)
else :
    print("Angka terbesar kedua :", angka5)