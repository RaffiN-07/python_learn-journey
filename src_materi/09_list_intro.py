# Ini adalah episode 29 Kelas Terbuka
# Pembelajaran list

#==========LIST===============

#Kumpulan data Integer
data_integer = [1,3,4,2,5,9,6]
print(data_integer)
print(type(data_integer[2]))


print(f"\n{"="*20}")
#Kumpulan data String
data_string = ["raffi","ica","coding","cyber security"]
print(data_string)
print(type(data_string[0]))


print(f"\n{"="*20}")
#Kumpulan data Boolean
data_bool = [True,False,True,True,False,False]
print(data_bool)
print(type(data_bool[4]))


print(f"\n{"="*20}")
#Kumpulan data float
data_float = [3.14,1.5,0.5]
print(data_float)
print(type(data_float[1]))


print(f"\n{"="*20}")
#Kumpulan data campuran
data_campuran = [2,True,10,False,3.14,"otong","raffi"]
for data in data_campuran:
  print(f"Tipe data {[data]} adalah {type(data)}")

print(f"\n{"="*20}")

# cara alternatif membuat list memakai range 
data_range = range(0,10,3) #dalam range(start,stop,step)
data_list = list(data_range)
print(data_list)
print(f"\n{"="*20}")

# list menggunakan for loop
list_forloop = [i**3 for i in range(0,10)]
print(list_forloop)
print(f"\n{"="*20}")

# List menggunakan for loop & if
list_forloop_if_ganjil = [i for i in range(0,10) if (i % 2) != 0]
list_forloop_if_genap = [i for i in range(0,10) if (i % 2) == 0]
print(list_forloop_if_ganjil)
print(list_forloop_if_genap)

print(f"\n{"="*20}")
"""
Study Case ("menentukan angka Ganjil dan Genap dalam list")
"""

data_angka = [1,2,3,4,5,6,7,8,9,10]

for angka in data_angka:
  if (angka % 2) == 0 :
    print(f"{angka} adalah Genap")
  else:
    print(f"{angka} adalah Ganjil")
    
    