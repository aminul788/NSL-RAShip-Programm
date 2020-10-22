'''
    Date         : 22/10/2020
    Day          : Thursday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : Words Score
    Problem link : https://www.hackerrank.com/challenges/words-score/problem
'''

def is_vowel(letter):
    vowels = "aeiouy"
    return letter in vowels

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
            
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
        
    return score


n = int(input())
words = input().split()
print(score_words(words))


