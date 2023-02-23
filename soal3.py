#input
angka1 = int(input("Masukkan bilangan 1 : "))
angka2 = int(input("Masukkan bilangan 2 : "))
angka3 = int(input("Masukkan bilangan 3 : "))

#proses
#pembulatan angka 1
sisa_angka1 = angka1%10
if sisa_angka1 < 5 :
    pembulatan1 = angka1 - sisa_angka1
else :
    pembulatan1 = (angka1 - sisa_angka1) + 10

#pembulatan angka 2
sisa_angka2 = angka2%10
if sisa_angka2 < 5 :
    pembulatan2 = angka2 - sisa_angka2
else :
    pembulatan2 = (angka2 - sisa_angka2) + 10

#pembulatan angka 3
sisa_angka3 = angka3%10
if sisa_angka3 < 5 :
    pembulatan3 = angka3 - sisa_angka3
else :
    pembulatan3 = (angka3 - sisa_angka3) + 10

jumlah = pembulatan1 + pembulatan2 + pembulatan3

#output
print(f'{pembulatan1} + {pembulatan2} + {pembulatan3} = {jumlah}')