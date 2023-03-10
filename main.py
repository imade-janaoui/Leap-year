
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return leap
        else:
            return True
    else:
        return leap
    # Write your logic here

    return leap


year = int(input("give me a year:"))
if is_leap(year) ==True:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


