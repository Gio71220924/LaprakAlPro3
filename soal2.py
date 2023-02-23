#input
bilangan1 = str(input("Masukkan bilangan 1 (2 digit) : "))
bilangan2 = str(input("Masukkan bilangan 2 (2 digit) : "))

angka1_pertama = bilangan1[0]
angka2_pertama = bilangan1[1]
angka1_kedua = bilangan2[0]
angka2_kedua = bilangan2[1]

if angka1_pertama == angka1_kedua or angka1_pertama == angka2_kedua :
    print("Sama")
elif angka2_pertama == angka1_kedua or angka2_pertama == angka2_kedua :
    print("Sama")
else :
    print("Tidak sama")