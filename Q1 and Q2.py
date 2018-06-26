#Q1andQ2

arr = map(str,raw_input("Enter list to print pattern :").split())

n = len(arr)
j = n/2
for i in range(n/2, 0, -1):
    if i == n/2:
        print " "*(n) + str(arr[n/2])
        
    print  " "*(n-j-1) + str(arr[i-1]) +"  "*(n-i-1) + str(arr[j+1])
    j += 1
    
    

