a=0
while a <= 99:
  a=a+1
  if a%7==0 or a%10==7 or a in range(70,80):
     print("failed! u check the {}".format(a))
  else:
     continue
