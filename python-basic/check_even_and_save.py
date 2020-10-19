
## User input
limit = int(input("Enter the limit: "))

# def is_even(x):
#     return x % 2 == 0

# user_number = range(1,limit+1)
# filter_even = filter(is_even, user_number)
# even_list  = list(filter_even)

## using lambda function 
even_list = list(filter(lambda x: x%2 == 0, range(1,limit+1)))


## saving the even list as a text file
with open("even_list.txt", "w") as file:
    file.write("Toatal " + str(len(even_list)) + " Even Numbers Found.\nHere is the numbers:\n\t")
    even = 0
    for i in even_list:
        even += 1
        file.write(str(i)+'\n\t')
    