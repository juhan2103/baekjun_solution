word = list(input())
alphabet = list(map(chr, range(97, 123)))

answer = []
for a in alphabet:
    if a in word:
        answer.append(word.index(a))
    else:
        answer.append(-1)

for a in answer:
    print(a, end=' ')
