a,b,v=map(int,input().split())
num=(v-a)%(a-b)
day=(v-a)//(a-b)
if num==0:
    day+=1
else:
    day+=2
print(day)