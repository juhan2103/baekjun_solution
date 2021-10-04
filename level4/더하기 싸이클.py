a=int(input())
num=a
cycle=1
while(True):  
  try:
    if((a//10)+(a%10)>=10):
      a=(((a//10)+(a%10))+((a%10)*10))-10
    else:
      a=((a//10)+(a%10))+((a%10)*10)
    if(a==num):
      print(cycle)
      break
    else:
      cycle+=1
  except EOFError:
    break