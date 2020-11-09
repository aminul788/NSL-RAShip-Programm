'''
    Date         : 16/10/2020
    Day          : Friday
    Author       : Md. Aminul Islam
    Problem      : Random Number Generation, 
                   Count Frequency of the numbers
                   and save the frequency as a text file
'''

import random

random_num_list = [random.randrange(100, 1000, 100) for i in range(1000)]

## a function to count random numbers
def CountFrequency(num_list):
    frequency = {}
    for num in num_list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    sorted_frequency = sorted(frequency.items(), key = lambda x: x[1], reverse=True)
    dic = {i[0]:i[1] for i in sorted_frequency}

    for i in sorted_frequency:
        print(i[0], ':', i[1], 'times')


CountFrequency(random_num_list)