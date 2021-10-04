n = int(input())
for i in range(1, n+1):
    a, lst = input().split()
    for l in lst:
        print(l*int(a), end='')
    print()
