n = input()
m = len(n)
n = int(n)
for i in range(n):
    check = i
    for j in range(m+2):
        check += i//(10**j)%10
    if check == n:
        print(i)
        break
if i == n-1:
    print(0)