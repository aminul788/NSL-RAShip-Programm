#practice........................

# if 10 > 5:
#     print("10 greater than 5")
#     print("IF scope finished")

# print("Program ended")


# n = input("Enter the value: ")
# m = int(n)

# if (m % 2 == 0) :
# 	print(n + " is EVEN")
# else:
# 	print(n + " is ODD")


# num = int(input('Enter a number: '))

# if num > 0:
# 	print('{0} is Positive'.format(num))
# else:
# 	print('{0} is Negative'.format(num))

# a = "this is a cat"
# print(a.split(" "))


# b = int(input("enter a number"))
# c = 200 if(b>=100 and b<200) else 300
# print(c)


# for i in range(10):
# 	print(i)
# else:
# 	print("done")

# i = 0
# while 1 == 1:
#    print(i)
#    i = i + 1
#    if i >= 5:
#       print("Breaking")
#       break

# print("Finished")

#list.....
# number = 1
# my_numbers = [number, 2, 3]

# things = ["Numbers", 0, my_numbers, 4.56]
# print(things)



#for loop.................
# fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# # Lets make juice with these fruits

# for fruit in fruits:
#     print(fruit + " Juice!")	


# we need all of those three argumet, such as  start, stop, step
# def frange(start, stop, step):
#     i = start
#     while i < stop:
#         yield i
#         i += step
# for i in frange(0.5, 1.0 ,0.1):
#          print(i)


# for letter in 'Python': # Here "Python" acts like a list of characters
#     print(letter)



num = list(range(1,50))
even_list = []

#::::::::::evenlist without comprehension::::::::::::::::::::::

# for n in num:
# 	if n%2 == 0:
# 		even_list.append(n)
# print(even_list)

#::::::::::evenlist with comprehension::::::::::::::::::::::
# even_list = [n for n in num if n%2 == 0]
# print(even_list)

# even_list = [
# 	n
# 	for n in num
# 	if n%2==0

# ]



# matrix_1d = []
# matrix_2d = [[1,2,3],
# 			 [4,5,6]]

# for row in matrix_2d:
# 	for num in row:
# 		matrix_1d.append(num)

# print(matrix_1d)

# matrix_1d = [ num for row in matrix_2d for num in row]
# print(matrix_1d)


#:::::::::::removing vowel from a sentence::::::::::::::::

# vowels = 'aeiou'
# sentence = input("Enter your sentence: ")
# output_sentence = []

# # for letter in sentence:
# # 	if letter not in vowels:
# # 		output_sentence.append(letter)


# output_sentence =''.join([letter for letter in sentence if letter not in vowels])

# print("after removing the vowel your sentence are: "+ output_sentence)


#::::::::::::::::::: dictionary comprehension::::::
# fruit_ranking = [1, 2, 3]
# fruit_name = ['Mango', 'Pineapple', 'Watermelon']
# # fruit_rank_dict = {}

# # for i in range(len(fruit_ranking)):
# # 	fruit_rank_dict[fruit_ranking[i]] = fruit_name[i]


# fruit_rank_dict = { fruit_ranking[i]:fruit_name[i] for i in range(len(fruit_ranking))}

# print(fruit_rank_dict)


a = ["A","B","C","D","E","F"]

dic = { i+1:a[i] for i in range(len(a))}

print(dic)