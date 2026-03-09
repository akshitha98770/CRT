'''print all the factors of a given number
input : 12
output : 1 2 3 4 6 12

n = int(input("Enter a   number : "))
for i in range(1,n+1):
    if n % i == 0:
        print(i,end =" ")
print(n)  
'''
n =  int(input("Enter a number : "))
counter = 0
for i in range(1 , n // 2+1):
    if n % i == 0:
        counter += 1
print(counter+1)