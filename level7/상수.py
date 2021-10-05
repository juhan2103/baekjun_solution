num1, num2 = list(map(str, input().split()))
rev_num1 = num1[::-1]
rev_num2 = num2[::-1]
print(max(int(rev_num1), int(rev_num2)))
