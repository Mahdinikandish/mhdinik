year = int(input("sene khd ra vared knid: "))
month = int(input("mah ra vared knid : "))
day = int(input("rooz ra vared knid : "))
d = year*365 + month*30 + day
print(d)
#----------------------------

# ax**2 + bx + c
# x1 , x2 = ?
# x1 = -b + (b**2-4ac)**0.5
# x2 = -b - (b**2-4ac)**0.5
a = float(input('please enter a : '))
b = float(input("please enter b : "))
c = float(input("please enter c : "))
x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
print(x1,x2)
#-------------------------

import math
print(math.sin(math.pi))