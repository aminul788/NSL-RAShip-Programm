import random

random_num_list = [random.randrange(100, 1000, 100) for i in range (1000)]

# a function to count the random numbers and save as a text file
def CountFrequency(num_list):
    frequency = {}
    for num in num_list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1


    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    dic = {i[0]:i[1] for i in sorted_frequency}

    ## print the sorted frequency
    # for i in sorted_frequency:
	#     print(i[0], ':', i[1], 'times')

    ## genearally save a dictionary
    # f = open("count_frequency.txt","w")
    # f.write( str(sorted_frequency) )
    # f.close()

    # saving a dictionary line by line
    with open("count_frequency.txt", "w") as file:
        for k, v in dic.items():
            dictionary_content = str(k) + ": " + str(v) + "\n"
            file.write(dictionary_content)

    # # saving the file as csv
    # import csv
    # w = csv.writer(open("output.csv", "w"))
    # for key, val in dic.items():
    #     w.writerow([key, val])


CountFrequency(random_num_list)

