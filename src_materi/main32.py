## Copy List 

a = ["raffi","annisa","riza"]
print(f"a = {a}")

b = a # pass by reference 
print(f"b = {b}")

b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres dari kedua list
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")


# cara mencopy list menggunakan data.copy()

# mengambil duplikat list a dan memiliki address tersendiri
c = a.copy() # full duplicate / data baru

print(f"c = {c}")
print(f"address c = {hex(id(c))}")
c[2] = "subur"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")