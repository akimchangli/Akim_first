#1 Задача
n = int(input("Sisestage arv vahemikus 1 kuni 9:"))

for i in range(n):
    print("    /V\    ", end=" ")
print()

for i in range(n):
    print("   / V \   ", end=" ")
print()

for i in range(n):
    print("  / V V \  ", end=" ")
print()

for i in range(n):
    print(" /VV V VV\ ", end=" ")
print()

#2 Задача
result = 1

R = int(input("Sisestage R-number:"))

for i in range(R + 1):
    if i % 2 != 0:
        result *= i

print(f"Paaritute väärtuste korrutis 0 kuni {R}: {result}")


R=int(input("Sisestage R-number:"))
result=numbr(R)
print(f"Paaritute väärtuste korrutis 0 kuni {R}: {result}")

#3 Задача
import random

N = random.randint(1, 20)

arvs = [random.randint(-10, 10) for _ in range(N)]

positiivne = sum(1 for num in arvs if num > 0)

print(f"Loodud {N} numbrit: {arvs}")
print(f"Positiivsete arvude arv: {positiivne}")

#4 Задача
paarisarv = 0
paarituarv = 0

kasutaja_number = int(input("Sisestage naturaalarv: "))

while kasutaja_number > 0:
    digit = kasutaja_number % 10
    if digit % 2 == 0:
        paarisarv += 1
    else:
        paarituarv += 1
    kasutaja_number //= 10

print(f"Paarisarvud: {paarisarv}")
print(f"Paaritud arvud: {paarituarv}")
