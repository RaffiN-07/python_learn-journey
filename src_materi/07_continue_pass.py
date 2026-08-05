# continue and pass

# continue

angka = 0

print(f"{"="*5} Mulai Program {"="*5}\n Angka sekarang adalah -> {angka}")

while angka < 5:
  angka += 1
  print(f"\nAngka sekarang adalah -> {angka}")
  if angka % 2 == 0: # aksi 1
    print(f"{angka} merupakan bilangan genap")
    print("ini Aksi pertama genap")
    continue
  else:
    print(f"{angka} merupakan bilangan ganjil")
    print("ini Aksi pertama ganjil")
  print("Ini Aksi kedua") # aksi ini akan dilewati oleh continue di kondisi aksi 1 bilangan genap

print(f"\n{"="*7} PROGRAM SELESAI {"="*7}")

# Break

data_input = int(input("Hitung sampai: "))
angka = 0

while True:
  angka += 1
  print(f"Angka sekarang -> {angka}")
  if angka == data_input:
    print(f"angka {data_input} sudah selesai dihitung")
    break
  print("Lanjut hitung\n")

print(f"\n{"="*5} Program Finish {"="*5}")