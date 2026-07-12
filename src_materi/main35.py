# Loop list and enumerate

print('For Loop')

kumpulan_angka = [2,3,7,9,3,10]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

kumpulan_nama = ["raffi", "prabowo", "annisa", "riza", "yanti"]

for nama in kumpulan_nama:
    print(f"Nama: {nama}")

list_angka = [5,3,8,9,2,4,3]

panjang = len(list_angka)

for i in range(panjang):
    print(f"angka = {list_angka[i]}")

print("\n While loop")

i = 0

while i < panjang:
    print(f"angka = {list_angka[i]}")
    i += 1

any_list =[1,7,"raffi","kucing", 5.60, True]

[print(f"isi list = {i}") for i in any_list]

print("\n")

for index, isi_list in enumerate(any_list,start=1):
    print(f"{index} Isi List = {isi_list} dan \n dan bertype {type(isi_list)}")



angka_urut = [1,2,3,4,5,6,7,8,9,10]

angka_kuadrat = [print(f"Kuadrat dari {i} adalah = {i**2}") for i in angka_urut]

