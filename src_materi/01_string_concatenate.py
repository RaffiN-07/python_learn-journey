#Kelas terbuka episode 16
# operasi manipulasi string 
# 1. menyambung string (concatenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_terakhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_terakhir
print(str(nama_lengkap))

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + "= " + str(panjang))

# 3. operator untuk string 

# mengecek apakah ada komponen char atau string di dalam string

d = "d"
status = d in nama_lengkap
print(d + " dalam " + nama_lengkap + "= " + str(status))


