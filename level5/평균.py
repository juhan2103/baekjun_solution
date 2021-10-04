n = int(input())
li = list(map(int, input().split()))
re = []
sum = 0.0
avg = 0.0
for i in range(0, n):
    a = li[i]/max(li)*100
    re.append(a)
for i in range(0, n):
    sum += re[i]
avg = sum/n
print(avg)
