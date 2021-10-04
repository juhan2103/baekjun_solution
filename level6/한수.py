num = int(input())
lst = []
n = 1
count = 0
while n < num+1:
    if(n < 100):
        count += 1
    else:
        lst = []
        for i in str(n):
            lst.append(i)
        if str(int(lst[2])-int(lst[1])) == str(int(lst[1]) - int(lst[0])):
            count += 1
    n += 1
print(count)
