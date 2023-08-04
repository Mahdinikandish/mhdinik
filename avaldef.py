def is_prime(a):
    if a == 1:
        return False   
    if a == 2:
        return True     
    if a % 2 == 0 :
        return False
    i=2
    p=True
    while i < a :  
        if a % i ==0 :
            p = False
        i+=1
    return p   
a= int(input())
z= is_prime(a)
print(z)


