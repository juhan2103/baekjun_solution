T = int(input())
for i in range(0, T):
    H, W, N = map(int, input().split())

    height = N % H
    room = N//H

    if height == 0:
        height = H
        room -= 1

    if room+1 < 10:
        room = '0' + str(room+1)
    else:
        room = str(room+1)

    print("{}{}".format(height, room))
