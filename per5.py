def km(a):
    return a/1000

jarak = int(input('Masukkan Nilai dalam km: '))

print('jarak dalam km', km(jarak))




from nath import sprt

help(sprt)

b = input("Masukkan nilai yang akan di cari akarnya")
a = sprt(int(b))
print("hasilnya",a)


import mymodule

mymodule.hitung(2,2)

print("version dari module kita adalah : ",mymodule._version_)
