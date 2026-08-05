# FORMAT STRING

# contoh generic
# string
nama = "raffi"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"nilai bool = {boolean}"
print(format_str)

# angka
angka = 174.5
format_str = f"tinggi badan = {angka}"
print(format_str)

# bilangan bulat
bilangan_bulat = 15
format_str = f"bilangan bulat {bilangan_bulat:d}"
print(format_str)

# bilangan ribuan & jutaan
bilangan_ribuan = 2000
bilangan_jutaan = 6000000
format_rb= f"bilangan ribuan {bilangan_ribuan:,}"
format_jt = f"bilangan jutaan {bilangan_jutaan:,}" # otomatis akan menaruh titik sesuai banyak bilangan
print(format_rb)
print(format_jt)

# bilangan desimal
angka = 2005.43216
format_str = f"desimal = {angka:.2f}" # perintah 2f mengambil 2 angka dibelakang
print(format_str)

# menampilkan leading zero dan menambah angka
angka = 2005.43216
format_str = f"desimal = {angka:08.2f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 100.4321
format_minus = f"angka minus = {angka_minus:d}"
format_plus = f"angka plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persentase = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp{harga * jumlah:,}"
print(format_string)

# format pada angka lain (binary, octal, hexadecimal)
angka = 15
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)