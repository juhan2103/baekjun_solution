dial = ['1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '0']
word = input().upper()
time = 0

for i in word:
    for j in dial:
        if i in j:
            time += dial.index(j)+2
            break
print(time)
