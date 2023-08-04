n = int(input())
i = 0
for i in range(0 , n) :
    # print("*", end = "")
    j = 0
    for j in range(0,n) :
        if i == 0 or i == n-1 :
            print("*",end="")
        else :
            if j == 0 or j == n-1 :    
                print("*", end ="")
            else :
                print(" ", end= "")
    print()     