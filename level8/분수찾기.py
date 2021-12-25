n=int(input())
line=0
cnt=0
while n>cnt:
    line+=1
    cnt+=line
gap=cnt-n
if line%2==0:
    top=line-gap
    under=gap+1
else:
    top=gap+1
    under=line-gap
print(str(top)+"/"+str(under))