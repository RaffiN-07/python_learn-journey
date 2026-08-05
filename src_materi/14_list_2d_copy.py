data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

data = data_2D[0][1]

print(f"isi data adalah = {data}")

# address kedua data (asli dan copy)
print(f"address data 2D asli = {hex(id(data_2D))}")
print(f"address data 2D copy = {hex(id(data_2D_copy))}")


#addres member ke-1 
print("\n")
print("addres member ke-1")
print(f"address data 2D asli = {hex(id(data_2D[0][1]))}")
print(f"address data 2D copy = {hex(id(data_2D_copy[0][1]))}")


print("\n")
data_2D[1][0] = 7
data_2D[2] = 15
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

print("\n")
from copy import deepcopy
data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

# address kedua data (asli dan copy)
print(f"address data 2D asli = {hex(id(data_2D))}")
print(f"address data 2D deepcopy = {hex(id(data_2D_deepcopy))}")
print("\n")

print("addres member ke - 1")
print(f"address data 2D asli = {hex(id(data_2D[0][1]))}")
print(f"address data 2D deepcopy = {hex(id(data_2D_deepcopy[0][1]))}")

print("\n")

data_2D[0][1] = 90
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deepcopy = {data_2D_deepcopy}")
