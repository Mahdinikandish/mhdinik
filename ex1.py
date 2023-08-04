n = int(input())
revs_n = 0
while n > 0 :
    reminder = n % 10
    revs_n = (revs_n * 10) + reminder
    n = n // 10
print("{}".format(revs_n))
if n == revs_n :
        print ("Yes")
      else:
        print("No")    
