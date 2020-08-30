def d(n):
    m = int(n)
    for i in str(n):
        m += int(i)
    return m
n = input()
l = len(n)
n = int(n)
for k in range(max(1,n - 9*l),n+1):
    if d(k) == n:
        print(k)
        break
    if k == n:
        print(0)
