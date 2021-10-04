A = int(input())
B = int(input())
C = int(input())
li = []
mul = A*B*C
while mul > 0:
    li.append(mul % 10)
    mul = mul//10
for i in range(0, 10):
    print(li.count(i))
