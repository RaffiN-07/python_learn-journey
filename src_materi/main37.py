# List --> Array, mengakses data menggunakan index 

data_list = [2,3,5]

print(data_list[1]) # variabel[index data yang ingin diakses]

# dictionary -> associative array, 
# sebuah array yang jika ingin mengakses isi sebuah 
# datanya tidak lagi menggunakan index, tetapi 
# memakai identifier --> key

data_dict = {
    "key_1" : "values 1",
    "key_2" : "values 2"
} 

print(data_dict["key_1"])

print("\n")

data_nilai_otong ={
    "matematika" : 78,
    "b_indo" : 89,
    "B_ing" : 97,
    "ipa" : 92,
    "ips" : 93,
    "tik" : 100,
    "pjok" : 70
}

list_nilai = []

for i in data_nilai_otong:
    list_nilai.append(data_nilai_otong[i])

print(f"Update List Nilai: {list_nilai}")

rata_rata_nilai = sum(list_nilai) / len(list_nilai)
print(f"KKM = 80 \n Rata-rata Nilai Otong : {int(rata_rata_nilai)}")

print("\n")

data_siswa_otong = {
    "nama" : "Otong",
    "tanggal_lahir": "7 agustus",
    "kelas": 9,
    "nilai_kelas_9" : data_nilai_otong,
    "rata_rata_nilai" : int(rata_rata_nilai),
}

if rata_rata_nilai >= 80:
    print(f"=== SELAMAT ATAS NAMA SISWA {data_siswa_otong['nama']} LULUS! ===")
    for i in data_siswa_otong:
        print(f"{i} : {data_siswa_otong[i]}")
    print(f"{"="*35}")
else:
    print(f"===MOHON MAAF ATAS NAMA {data_siswa_otong['nama']} TIDAK LULUS!")
