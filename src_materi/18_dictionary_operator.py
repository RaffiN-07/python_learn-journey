# Operasi Dictonary
# Kelas Terbuka Eps 38


data_dict = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung"
}

# Menghitung panjang data 
LEN = len(data_dict)

print(f"panjang data dictionary: {LEN}")

print("\n")

#Mengecek key exist atau tidak
KEY = "cup"
CHECK_KEY = KEY in data_dict

print(f"key: {KEY} tersedia dalam data data_dict? \n = {CHECK_KEY}")

print("\n")

# mengakses value (read) dengan methode get
print(data_dict["dung"])

print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan")) # cek key dengan message tidak ditemukan 

print("\n")

# mengupdate value 
data_dict["dung"] = "roso suroso"
print(data_dict)
data_dict["cup"] = "rusdi surusdi"
print(data_dict)
## mengupdate value menggunakan methode update 
data_dict.update({"bowo": "prabowo"})
print(data_dict)
data_dict.update({"nyahu": "netanyahu"})
print(data_dict)

print("\n")

for nama_panggilan in data_dict:
    print(f"\nNama Panggilan : {nama_panggilan} \nNama Lengkap : {data_dict[nama_panggilan]} ")

print("\n")

# mendelete data dictionary menggunakan methode del
print(f"Data sebelum menghapus key 'nyahu' : \n {data_dict}")

## sesudah menghapus key nyahu
del data_dict["nyahu"]
print(f"Data sesudah meghapus key 'nyahu': \n{data_dict}")







