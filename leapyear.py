year = int(input("Year: "))
if (year %100) and (year % 400) == 0:
    print("{0} is a Leap year".format(year))
elif (year %100) and (year % 4) != 0:
    print("{0} is a Leap year".format(year))
else:
    print("{0} is not a Leap year".format(year))