'''
sample input : 1234
sample output : 4

sample input :12236
sample output : 5

t = int(input())
count = 0
while t > 0:
    count += 1
    t = t // 10
print(count)

n = int(input())
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit,end=" ")
    n = n // 10

def reverse(num):
    rev = 0
    while num> 0 :
        rev = (rev*10) + (num%10)
        num = num // 10
    return rev
n = reverse(int(input()))
while n > 0 :
    digit = n % 10
    if digit % 2 == 0:
        print(digit,end=" ")
    n = n // 10 
'''
n = int(input())
temp = reverse(n)
print(temp == n)
if temp == n:
    print(True)
else:
    print(False)
print(Ture) if temp == n else print(False)

