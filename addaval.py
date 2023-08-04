a = int(input())
b = int(input())
if a > b :
    a,b = b,a
n = a
# a a+1 ... b-1 b
while n <= b :
    i = 2
    p = True
    while i < n :
        if n % i==0 :
            p = False
        i+=1
    if p==True and n!=1 :
        print(n)
    n += 1
        