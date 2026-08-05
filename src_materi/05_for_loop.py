#Perulangan (Loop)

#For kondisi:
#   aksi

# ini dengan list
angka_list = [0,3,5,7,10] # ini adalah list
for i in angka_list:
  print(f"i sekarang adalah {i}")

print("Akhir dari program 1\n")

# ini dengan range

angka_range = range(1,5)
for i in angka_range:
  print(f"i sekarang adalah {i}")

print("Akhir dari program 2\n")

# contoh menyebutkan bil ganjil/genap
angka_range_2 = range(1,11)
for i in angka_range_2:
  if i % 2 == 0:
    print(f"angka {i} adalah bilangan genap")
  else:
    print(f"angka {i} adalah bilangan ganjil")

print("Akhir dari program 3")