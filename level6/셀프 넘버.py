num = 1
lst = []
while num < 10001:
    self_num = num
    for n in str(num):
        self_num += int(n)
    lst.append(self_num)
    num += 1

for x in range(1, 10001):
    if x not in lst:
        print(x)
