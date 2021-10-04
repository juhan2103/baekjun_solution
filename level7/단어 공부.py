word_dic = {}

word = input().upper()

for w in word:
    if w in word_dic:
        word_dic[w] += 1
    else:
        word_dic[w] = 1

cnt = 0
answer = 0

for key, value in word_dic.items():
    if int(cnt) < value:
        cnt = value
        answer = key
    elif int(cnt) == value:
        answer = "?"

print(answer)
