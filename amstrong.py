def is_armstrong_number(number):
  totalDigits = len(str(number))
  sum = 0
  temp = number
  while temp>0:
    reminder = temp%10
    sum += reminder**totalDigits
    temp//=10
  return number==sum

print(is_armstrong_number(153))
    
