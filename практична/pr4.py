import math

a = float(input("Введіть значення a :"))
b = float(input("Введіть значення b :"))
c = float(input("Введіть значення c :"))

D = b**2 - 4*a*c

if D < 0:
    print("Розвязку немає")
elif D == 0:
    x = -b / (2*a)
    print(f"{x}")
else:
    x1 = (-b + math.sqrt(D)) / (2*a)  #math.sqrt(D) взяв форумулу дискримінанта з інету
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"{x1} , {x2}")
