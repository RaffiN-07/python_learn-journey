#Latihan perulangan membuat segitiga

sisi = 10

# dummy variable
count = 1

# 1. Menggunakan For Loop
print("Awal for")
for i in range(sisi):
  print("*"*count)
  count +=1
print("Akhir for")

print('\n')

# 2. Menggunakan While Loop
print("Awal While")
count = 1
while True:
  print("*"*count)
  count += 1
  if count > sisi:
    break
print("Akhir While")

print("\n")

# 3. Hanya ganjil saja
print("Awal ganjil")
count = 1
spasi = int(sisi/2)
while True:
  if (count%2):
    # misal count = 1 akan di % 2 = 1,
    # 1 dalam biner berarti True (mengekseskusi program)
    print(" "*spasi ,"+"*count)
    count += 1
    spasi -= 1
  else:
    count += 1
    # count bertambah 1 misal 2 akan di % 2 = 0
    # 0 dalam biner berarti False (masuk kedalam else)
    continue
  if count > sisi:
    break
print("Akhir ganjil")

print('\n')

# 4. Hanya genap saja
print("Awal genap")
count = 1
while True:
  if (count % 2 == 0):
    print("*"*count)
    count += 1
  else:
    count += 1
    continue
  if count > sisi:
    break
print("Akhir Genap")