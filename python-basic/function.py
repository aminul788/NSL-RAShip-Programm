# n = 0
# while n>0:
#     year = int(input("Enter a year: "))
#     is_leap(year)



# # year = int(raw_input())

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = True
    else:
        leap = False

    return leap

n = 1
while n > 0:
    year = int(input("Enter a year: "))
    
    print (is_leap(year))