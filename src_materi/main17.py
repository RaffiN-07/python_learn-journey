# Kelas Terbuka  Eps 17
# Operasi dan manipulasi string part (2)

# operator dalam bentuk method

## merubah case dari string

# merubah semua ke upper case
salam = "bro!"
salam = salam.upper()
print("normal = " + salam)
print("upper = " + salam)
salam = salam.upper()

# merubah semua ke lower case
salam = "HaY nAMaKU RaFFi"
salam = salam.lower()
print("lower = " + salam)


## pengecekan dengan isX method
# contoh pengecekan dengan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
huruf = "raffi"
print(huruf + " merupakan huruf = " + str(huruf.isalpha()))

# isalnum() <-- mengecek huruf dan angka
huruf_angka = "nugraha07"
print(huruf_angka + " huruf dan angka  = " + str(huruf_angka.isalnum()))


# isdecimal() <-- angka saja
angka = "07"
print(angka + " merupakan angka  = " + str(angka.isdecimal()))

# isspace() <-- spasi, tab, newline, \n
sepasi = " "
print(sepasi + " merupakan space/tab/newline  = " + str(sepasi.isspace()))

# istitle()
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

# startswith.()
cek_start = "Muhammad Raffi Nugraha".startswith("Muhammad")
print("starts = " + str(cek_start))

# endswith.()
cek_start = "Muhammad Raffi Nugroho".endswith("Nugroho")
print("ends = " + str(cek_start))


## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ekhm '.join(pisah)
print(gabungan)

gabungan = "akuekhmsayangekhmkamu"
print(gabungan.split('ekhm')) # akan menjadi list kembali


# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(20, "-")
print("'" + tengah + "'")

# kebalikannya > strip()
tengah = tengah.strip("-")
print("'" + tengah + "'")

kanan = kanan.strip()
print("'" + kanan + "'")

kiri = kiri.strip()
print("'" + kiri + "'")