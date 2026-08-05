data_0 = [1,2]
data_1 = [3,4,5]

list_biasa = [1,2,3,4]

print(f"ini adalah list biasa {list_biasa}")

list_2d = [data_0,data_1, list_biasa]

print(f"ini adalah nested list {list_2d}")


#contoh pengunaan nested list

peserta_0 = ["raffi",17,"laki-laki"]
peserta_1 = ["annisa",40,"perempuan"]
peserta_2 = ["prabowo",18,"laki-laki"]
peserta_3 = ["megawati",60,"perempuan"]
peserta_4 = ["gibran",72,"laki-laki"]


list_peserta = [peserta_0, peserta_1,peserta_2,peserta_3,peserta_4]

print(f"Data peserta adalah: \n {list_peserta}")

print("\n")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Jenis kelamin\t: {peserta[2]}\n")

# dengan reference copy

list_copy = list_peserta.copy()

print(f"Peserta = {list_copy}")

peserta_0[0] = "jokowi"
print(f"Peserta = {list_copy}")
print(f"Peserta = {list_peserta}")

print("\n")

for peserta in list_copy:
    if peserta[1] >= 60 :
        print(f"Nama\t : {peserta[0]}")
        print(f"Jenis kelamin\t : {peserta[2]}")
        print(f"Status Bansos\t : Memenuhi, \n Karena Umur Berusia {peserta[1]} \n sudah memasuki masa lansia\n")
    else:
        print(f"Nama\t : {peserta[0]}")
        print(f"Jenis kelamin\t : {peserta[2]}")
        print(f"Status Bansos\t : Tidak Memenuhi, \n Karena Umur Berusia {peserta[1]} \n masih muda")