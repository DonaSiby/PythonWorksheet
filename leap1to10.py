lower = 1
upper = 10
print("Prime numbers between" ,upper, "and" ,lower, ":")
for num in range(lower,upper+1):
  if num>1:
    for i in range(2,num):
      if(num%i)==0:
        break
    else:
      print(num)
