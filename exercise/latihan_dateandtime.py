# Date and Time (latihan)

import datetime as dt

# contoh sintaks
hari_ini = dt.date.today()
print(hari_ini)

print(f"hari ini hari adalah hari = {hari_ini:%A}")

tanggal = dt.date(2007,7,6)
print(tanggal)

print(f"hari tanggal tersebut hari apa = {tanggal:%A}")



# Latihan

print("Silahkan masukkan tanggal, \nbulan, dan tahun lahir anda\n")

tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"Hari pada tanggal lahir adalah : {tanggal_lahir:%A}")
print(f"Umur anda sekarang adalah: \n{umur_tahun} tahun, {umur_bulan} bulan, {umur_hari.days} hari")
 
 