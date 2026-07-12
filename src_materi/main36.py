# tipe colecttions 

'''
<--- 1. List --->
'''

# Sifat List:
# data bisa diubah, ada indexing, paling fleksibel
# bisa banyak menggunakan method 

data_list = [1,2,3,4,5,6]

print(f" {"="*5} Data List {"="*5} ")
print(data_list)
print(f"Tipe data: {type(data_list)}")

# contoh fitur list

## mengakses index dan mengubah index 

for index, data in enumerate(data_list):
    print(f"Mengakses Index Ke-{index} \n dan isi data adalah: {data}")

data_list[2] = 10
print(f"mengubah data Index ke 2 Menjadi {data_list[2]} \n List Update: {data_list}")



'''
<---2. Tuple ---->
'''

# Sifat Tuples:
# data tidak bisa diubah/diganti, 
# indexing masih berlaku
# masih mempunyai method nya sendiri

data_tuples = (
    "apple","watermelon", "blueberry", "banana", "coconut"
    )

print(f"\n{"="*5} Data Tuples {"="*5} ")
print(data_tuples)
print(f"Tipe data: {type(data_tuples)}")

# contoh fitur list

## mengakses index dan mengubah index 
for index, data in enumerate(data_tuples):
    print(f"Mengakses Index Ke-{index} \n dan isi data adalah: {data}")

## unpack tuples 
(red, red_green, blue, yellow, green) = data_tuples
print("---Unpack tuples---")
print(red)
print(red_green)
print(yellow)


'''
<--- 3.Sets --->
'''

# Sifat sets:
# mirip seperti list namun memiliki kekurangan yaitu:
# tidak memiliki indexing (sperti himpunan),
# namun masih bisa menggunakan method append, count, pop, dll

data_sets = {1,2,3,4,5,6}

print(f"\n{"="*5} Data Sets {"="*5} ")
print(data_sets)
print(f"Tipe data: {type(data_sets)}")


## contoh fitur list 

### menggunakan method add untuk menambahkan data
data_sets.add(7)
print("---Add Method---")
print(data_sets)





