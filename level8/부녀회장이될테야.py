test = int(input())
for _ in range(test):
    floor = int(input())
    room = int(input())

    lst = [i for i in range(1, room+1)]
    for k in range(floor):
        for n in range(1, room):
            lst[n] += lst[n-1]
    print[lst[-1]]
