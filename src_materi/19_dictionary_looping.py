# Kelas Terbuka Eps 40 
# Looping Dictionary

teman_teman = {
    "ucup" : "surucup",
    "otong" : "surotong",
    "dung" : "surudung",
    "sep" : "asp surasep",
    "cuy": "surucuy"
}

## looping dictionary tanpa menggunakan methode
for teman in teman_teman:
    print(f"{teman} \t: {teman_teman[teman]}")

print("\n")

## operator untuk mengambil item / iterables 

### method iterables untuk mengambil keys 
keys = teman_teman.keys()
print(f"keys : {keys}") 

print("\n")

## looping dictionary menggunakan methode keys 
for key in teman_teman.keys():
    print(f"{key} \t: {teman_teman.get(key)}")

print("\n")

### method iterables untuk mengambil values
values = teman_teman.values() 
print(f"values: {values}")

print("\n")

## looping dictionary menggunakan methode values 
for values in teman_teman.values():
    print(f"values: {values}")

print("\n")

## mengakses data menggunakan methode .items() 
items = teman_teman.items()
print(items) 

print("\n")

## looping dictionary menggunakan methode .items() 
for item in teman_teman.items():
    print(item)


print("\n")

## looping menggunakan methode items,
## menambahkan variable key dan values dalam iterasi
for key, values in teman_teman.items():
    print(f"key = {key}\t values = {values}")
