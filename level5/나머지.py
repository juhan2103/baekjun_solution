li = []
for i in range(1, 11):
    a = int(input())
    li.append(int(a % 42))
li = set(li)
print(len(li))
