'''
    Date         : 02/11/2020
    Day          : Monday
    Author       : Md. Aminul Islam
    Topic        : Problem Solving
    Problem      : The Minion Game
    Problem link : https://www.hackerrank.com/challenges/the-minion-game/problem
'''
def minion_game(string):
    ### using mathemetical equation: n+(n-1)+(n-2)+.....+2+1 = n(n+1)/2
    # vowels = "AEIOU"
    # slen = len(string)
    # totalsub = int(slen * (slen + 1) / 2)
    # kevin_score = sum(slen - i for i in range(slen) if string[i] in vowels)   
    # stuart_score = totalsub - kevin_score
    

    ### by producing all the sub strings but for large string it get runtime error
    # def subs(txt, startswith):
    #     score = 0
    #     for i in range(len(txt)):
    #         for j in range(1, len(txt) - i + 1):
    #             if txt[i] in startswith:
    #                 score += 1
    #     return score

    # vowels = 'AEIOU'
    # consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    # kevin_score = subs(string, vowels)
    # stuart_score = subs(string, consonants)


    ### using another logic
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevin_score += (len(string)-i)
        else:
            stuart_score += (len(string)-i)


    ## conditions
    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif kevin_score < stuart_score:
        print('Stuart', stuart_score)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)




