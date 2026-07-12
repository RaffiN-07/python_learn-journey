## Operasi 

#Index  0(-3)     1(-2)     2(-1)
data = ["Ucup","Otong","budi"]

data_0 = data[0]

print(f"Data pertama (index-0) = {data_0}")


# Mengambil info jumlah/panjang data di dalam list 

print(f"Panjang data dalam list adalah {len(data)}")


## Manipulasi data list 

# Menambahkan item ke dalam data list (sesuai posisi)
print(f"data sebelum ditambah {data}")

# Format data.insert(index keberapa data ingin diselipkan,isi data)
data.insert(2,"Rapi")
print(f"data setelah ditambah {data}")

# Menambah data di akhir list 
data.append("kucing")

print(f"data setelah ditambah {data}")

# menambahkan list dengan list baru
data_baru = [1,2,3,4,5]
data.extend(data_baru)

print(f"data gabungan: \n{data}")


## Merubah data 
# contoh mengubah isi data index ke 3
data[3] = 3.14
print(f"Perubahan data: \n{data}")

# me-remove data
data.remove("kucing")
print(f"Perubahan data: \n{data}")

# me-remove data paling belakang
data_akhir = data.pop()
print(f"Perubahan data: \n{data}")
print(f"data akhir adalah {data}")

print("\n")

#Penggunaan For loop untuk menampilkan semua index dan isi data
# dan penggunaan Conditonal if else sederhana untuk pengkondisian index terakhir
for indeks, isi_data in enumerate(data):
    if indeks == len(data) - 1:
        print(f"data terakhir atau indeks ke - {indeks} adalah {isi_data}")
    else:
        print(f"data indeks ke - {indeks} adalah {isi_data}")
