# If dan Else statement

# syarat membuat coontrol flow menggunakan if else statement :
# 1. if nya
# 2. kondisinya
# 3. aksinya

input_nama = str(input("Siapa nama anda? "))

# 1. Program if inline
#if input_nama == "ucup": print(f"Kamu ganteng sekali wahai {input_nama}")
#print(f"Terimakasih {input_nama}")

# 2. program if indentation
if input_nama == "ucup":
  print("kamu ganteng abiezz")
  print("dan kamu juga keren banget")
print(f"Terimakasih {input_nama}")

# 3. else statement

if input_nama == "otong":
  print(f"hai {input_nama}, si keren abiezz")
else:
  print(f"yah si {input_nama} mah ga keren, kamu tuh bukan otong")
print("akhir dari program")