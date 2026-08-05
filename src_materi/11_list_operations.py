## Operasi List
data_angka = [1,3,2,3,5,7,9,7,10,9,100,3]

print(f"Data angka adalah: \n {data_angka}")


# Count data (Jumlah data)
jumlah_data_3 = data_angka.count(3)
jumlah_data_7 = data_angka.count(7)
print(f"Jumlah angka 3 {jumlah_data_3}\n Jumlah angka 7 {jumlah_data_7}")


# Mengetahui posisi index data 
print("\n")

data_hewan = ["kucing", "anjing", "sapi", "kambing", "kelinci", "singa"]
print(f"Data Hewan:\n {data_hewan}")

index_ayam = data_hewan.index("anjing")
print(f"Index ayam adalah ke - {index_ayam}")
print(f"Index kelinci adalah ke - {index_ayam}")

#Mengurutkan List
print("\n")
print(f"Data sebelum di urut: \n {data_angka}")
data_angka.sort()
print(f"data setelah di urutkan:\n {data_angka}")

print("\n")
print(f"Data sebelum di urut: \n {data_hewan}")
data_hewan.sort()
print(f"data setelah di urutkan:\n {data_hewan}")

# membalik list data.reverse()
print("\n")
data_angka.reverse()
data_hewan.reverse()
print(f"data angka dan hewan setelah dibalik urutannya:\n {data_angka} \n {data_hewan}")
