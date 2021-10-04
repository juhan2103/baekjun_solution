n = int(input())
anw = []
for i in range(1, n+1):
    cnt = 0
    li = list(map(int, input().split()))
    avg = sum(li[1:])/li[0]
    for j in li[1:]:
        if(j > avg):
            cnt += 1
    anw.append("{:.3f}%".format(cnt/li[0]*100))
for data in anw:
    print(data)
