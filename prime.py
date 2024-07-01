num = int(input("Number: "))
flag = False
if num == 1:
    print(f"{num} - Not a prime Number")
elif num > 1:
    for i in range(2,num):
        if (num%i)==0:
            flag=True
            break
if flag:
    print(f"{num} - Not a prime Number")
else:
    print(f"{num} - Prime Number")
        