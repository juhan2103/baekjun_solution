n = int(input())
li = []
for i in range(0, n):
    li.append(str(input()))

for data in li:
    score = 0
    num = 0
    for i in data:
        if i == 'O':
            num += 1
            score += num
        else:
            num = 0
    print(score)
