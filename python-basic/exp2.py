
# Dictionary Comprehension
# Two list to a Dectionary


fruit_rank = [1,2,3]

fruit  = ['Mango','Apple','Orange']

fruit_dict = {
	fruit_rank[i] : fruit[i]
	for i in range(len(fruit_rank))
}

print(fruit_dict)
print("\n\n")


#Remove vowel from a sentence
print("Removing vowel from a sentence.")
vowel = 'aeiou'

sentence = input("Enter a sentence: ")

filtered_sentence = ''.join([

	letter
	for letter in sentence
	if letter not in vowel

	])

print(filtered_sentence)

#

