n = int(input())
i = 0
while i < n :
    # print("*", end = "")
    j = 0
    while j <n :
        if i == 0 or i == n-1 :
            print("*",end="")
        else :
            if j == 0 or j == n-1 :    
                print("*", end ="")
            else :
                print(" ", end= "")
        j += 1
    print()     
    i+=1           