a = int(input("enter num : "))
b = 0
while a != 0 :
    d = a % 10
    a = a // 10
    b = b*10 + d
a = b
b = 0
while a != 0 :
    d = a % 10
    a = a // 10
    # b = b*10 + d
    print(f"{d}: ",end="")
    i = 0
    while i < d:
        print(d,end="")
        i=i+1
    print()    
    






