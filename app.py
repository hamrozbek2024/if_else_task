# 1-masala
yosh = int(input("1-masala: Yoshingizni kiriting: "))
if yosh >= 18:
    print("Kattasisiz")
else:
    print("Kattasiz emas")
print("------------------------")


# 2-masala
a = int(input("2-masala: 1-sonni kiriting: "))
b = int(input("2-masala: 2-sonni kiriting: "))
if a > b:
    print("Birinchi son katta")
else:
    print("Ikkinchi son katta")
print("------------------------")


# 3-masala
son = int(input("3-masala: Son kiriting: "))
if son > 0:
    print("Musbat son")
else:
    print("Manfiy son")
print("------------------------")


# 4-masala
raqam = int(input("4-masala: Raqam kiriting: "))
if raqam < 10:
    print("10 dan kichik")
elif raqam == 10:
    print("10 ga teng")
else:
    print("10 dan katta")
print("------------------------")


# 5-masala
a = int(input("5-masala: 1-sonni kiriting: "))
b = int(input("5-masala: 2-sonni kiriting: "))
if a == b:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")
print("------------------------")


# 6-masala
matn = input("6-masala: Matn kiriting: ")
if matn == "hello":
    print("Salom!")
elif matn == "bye":
    print("Xayr!")
else:
    print("Noma'lum so'z")
print("------------------------")


# 7-masala
a = int(input("7-masala: 1-son: "))
b = int(input("7-masala: 2-son: "))
c = int(input("7-masala: 3-son: "))
if a >= b and a >= c:
    eng_katta = a
elif b >= a and b >= c:
    eng_katta = b
else:
    eng_katta = c
print("Eng katta son:", eng_katta)
print("------------------------")


# 9-masala
a = int(input("9-masala: 1-son: "))
b = int(input("9-masala: 2-son: "))
c = int(input("9-masala: 3-son: "))
if a <= b and a <= c:
    eng_kichik = a
elif b <= a and b <= c:
    eng_kichik = b
else:
    eng_kichik = c
print("Eng kichik son:", eng_kichik)
print("------------------------")


# 10-masala
raqam = int(input("10-masala: Raqam kiriting: "))
if raqam == 0:
    print("0")
elif raqam == 1:
    print("1")
else:
    print("Boshqa raqam")
print("------------------------")


# 11-masala
a = int(input("11-masala: 1-tomon: "))
b = int(input("11-masala: 2-tomon: "))
if a == b:
    print("Kvadrat")
else:
    print("To‘rtburchak")
print("------------------------")


# 12-masala
son = int(input("12-masala: Son kiriting: "))
if son <= 100:
    print("Kichik yoki teng 100")
else:
    print("Katta")
print("------------------------")
