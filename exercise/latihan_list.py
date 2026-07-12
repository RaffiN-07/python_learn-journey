# latihan list eps 36 kelas terbuka 

"""
<------------------------->
Bagian Judul dan Watermark
<------------------------->
"""

def watermark():
    print("""
####   ###  ##### ##### ##### 
#   # #   # #     #        #  
####  ##### ####  ####    #   
#  #  #   # #     #      #    
#   # #   # #     #     ##### 
""")

watermark()


def judul():
    print("""
==============
RAFFZ LIBRARY
==============
""")
judul()



"""
<=======================>
Bagian Main Logic Sistem 
<=======================>
"""


list_buku =[]

while True:
    def pilihan():
        print("""
=======================              
---------MENU----------
1. Tambah Data Buku
2. Lihat Data Buku anda
3. Keluar
-----------------------
=======================                            
""")

    pilihan()
    try:
        input_pilihan = int(input("[*] Masukkan Pilihan: "))
    except ValueError:
        print("[!] Masukkan Angka Yang Benar! ")
        continue


# 1. Main Logic Bagian Tambah Data Buku
    if input_pilihan == 1:
        
        while True:
            print("""
================
TAMBAH DATA BUKU
================                                    
""")
           
            data_judul = input("Judul Buku: ") 
            data_penulis = input("Nama Penulis: ")

            data_buku = [data_judul, data_penulis]
            list_buku.append(data_buku)


            print("No.\t| Judul\t\t| Penulis")

            for index, buku in enumerate(list_buku, start=1):
                print(f"{index}.\t| {buku[0]}\t| {buku[1]}")
            
            print("\n")

            verif_penambahan_data = input("[?] Apakah anda ingin menambahkan data lagi? y/n: ")
            if verif_penambahan_data == "y":
                continue
            else:
                break


# 2. Main Logic Bagian Lihat Data Buku
    elif input_pilihan == 2:
        if len(list_buku) == 0:
            print("[!] Tidak ada Buku yang diberikan")
            continue
        else:
            print("""
    ====================
    LIHAT DATA BUKU ANDA:
    1. Baca Di Tempat
    2. Pinjam Buku
    ====================
    """)
            try:
                pil_lihat_data =int(input("[*] Masukkan Pilihan: "))
            except ValueError:
                print("[!] Masukkan Angka Yang Benar! ")

## 2.1 Jika User ingin membaca di tempat,
## Maka Buku Tetap disimpan dalam data Database
            if pil_lihat_data == 1:
                print("No.\t| Judul\t\t| Penulis")
                for index, buku in enumerate(list_buku, start=1):
                    print(f"{index}.\t| {buku[0]}\t| {buku[1]}")
                masukkan_baca_ditempat = int(input("Pilih Buku Yang Ingin dibaca: "))
                if 1 <= masukkan_baca_ditempat <= len(list_buku):
                    indeks_buku = masukkan_baca_ditempat - 1
                    buku_dipilih = list_buku[indeks_buku]
                    keluaran_buku_dipilih = f"""
------------------------
Kamu Sedang Mebaca Buku:
Judul Buku\t: {buku_dipilih[0]}
Penulis Buku\t: {buku_dipilih[1]}
------------------------
Selamat Membaca!
"""
                    print(keluaran_buku_dipilih)
                else:
                    print("[!] No Buku Tidak Temukan")
                    continue


##2.2 Jika User ingin meminjam Buku
            if pil_lihat_data == 2:
                print("No.\t| Judul\t\t| Penulis")
                for index, buku in enumerate(list_buku, start=1):
                    print(f"{index}.\t| {buku[0]}\t| {buku[1]}")
                
                masukkan_bawa_pulang = int(input("[!] Pilih No Buku yang ingin dipinjam: "))
                if 1 <= masukkan_bawa_pulang <= len(list_buku):
                    indeks_buku = masukkan_bawa_pulang - 1
                    buku_dipilih = list_buku.pop(indeks_buku)
                    keluaran_buku_bawapulang = f"""
    ------------------------
    Kamu Meminjam Buku:
    Judul Buku\t: {buku_dipilih[0]}
    Penulis Buku\t: {buku_dipilih[1]}
    ------------------------
    Jangan lupa Kembalikan!
    """
                    print(keluaran_buku_bawapulang,"\n")
                    print("-----Update Data buku-----")
                    print("No.\t| Judul\t\t| Penulis")
                    for index, buku in enumerate(list_buku, start=1):
                        print(f"{index}.\t| {buku_dipilih[0]}\t| {buku_dipilih[1]}")
                else:
                    print("[!] No Buku Tidak Temukan")
                    continue

# 3. main logic Jika user ingin keluar dari sistem
    elif input_pilihan == 3:
        print("\n Terimakasih telah berkunjung!")
        break
    
    else:
        print("[!] Masukkan Angka yang benar!")
        continue
                
            


















