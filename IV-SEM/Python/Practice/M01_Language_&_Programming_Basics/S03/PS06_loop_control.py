'''
for i in range(1,11):
    print(i)
    if i == 5:
        continue
    print(i)
'''
p1 = "Akshu@115.."
for i in range(3):
    p2 = input()
    if p1 == p2:
        print("login successfully")
        break
else:
    print("Account was locked")