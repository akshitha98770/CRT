'''
li = [1,2,3,4,5]
# output: [1,4,9,16,25]
res = []
for i in li:
    res.append(i ** 2)
print(res)

ans = [i ** 2 for i in li]
print(ans)

li = [1,2,3,4,5]
#output: [2,4]
res = []
for i in li:
  if i%2==0:
    res.append(i)
print(res)

ans = [i for i in li if i%2==0]
print(ans)

print(" * "*5)

li = ['a','b','c']
#output: 'a b c'
res = " "
for ch in li:
    res = res + ch + " "
print(res) 

print(" ".join(li))


1.pyramid pattern
n = 4
#output :
   *
  * *
 * * *
* * * *

n = int(input())
for i in range(1,n+1):
  print(" "*(n -i)+"* "*i)
print("----------------")
for i in range(n,0,-1):
  print(" "*(n -i)+"* "*i)

2.daimond pattern
n = 4
#output:
   *
  * *
 * * * 
* * * *
 * * *
  * *
   *

n = int(input())
for i in range(1,n+1):
  print(" "*(n -i)+"* "*i)
for i in range(n,0,-1):
  print(" "*(n -i)+"* "*i)




3.number pyramid
n = 4
#output:
   1
  1 2
 1 2 3
1 2 3 4
'''
n = int(input())
for i in range(1,n+1):
  print(" "*(n-i)+" ".join([str(j)for j in range(1,i+1)]))
