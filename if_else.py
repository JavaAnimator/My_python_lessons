n1 = int(input("firts number: "))
n2 = int(input("second number: "))
if n1 == n2:
    print("The numbers are same")
#2 task
son = int(input("Juft son kiriting: "))
if son >= 10:
    print("Raxmat")
elif son < 10:
    print("Bu juft son emas")
#3 task
yosh = int(input("Yoshingizni kiriting: "))
if yosh <= 4 or yosh >= 60:
     print("Sizga kirish bepul ")
elif yosh <= 18:
     print("Sizga kirish 10ming so'm")
elif yosh > 18:
     print("Sizg kirish 20ming so'm")
#task 4

#menuni list
menu = ['olma', 'banan', 'tuxum', 'mandarin', 'limon']
ovqat = input("1 chi ovqatni kiriting: ")
ovqat2 = input("2 chi ovqatni kiriting: ")
ovqat3 = input("3 chi ovqatni kiriting: ")
ovqat4 = input("4 chi ovqatni kiriting: ")
ovqat5 = input("5 chi ovqatni kiriting: ")
# har biri uchun alohida if else ko'rsatib o'tildi
if ovqat.lower() in menu:
    print(f"Do'konda {ovqat} bor")
else:
    print(f"Do'konda {ovqat} yo'q")

# har bir input uchun alohida if else ko'rsatib o'tildi
if ovqat2.lower() in menu:
    print(f"Do'konda {ovqat2} bor")
else:
    print(f"Do'konda {ovqat2} yo'q")

# har bir input uchun alohida if else ko'rsatib o'tildi
if ovqat3.lower() in menu:
    print(f"Do'konda {ovqat3} bor")
else:
    print(f"Do'konda {ovqat3} yo'q")

# har bir input uchun alohida if else ko'rsatib o'tildi
if ovqat4.lower() in menu:
    print(f"Do'konda {ovqat4} bor")
else:
    print(f"Do'konda {ovqat4} yo'q")

# har bir input uchun alohida if else ko'rsatib o'tildi
if ovqat5.lower() in menu:
    print(f"Do'konda {ovqat5} bor")
else:
    print(f"Do'konda {ovqat5} yo'q")
