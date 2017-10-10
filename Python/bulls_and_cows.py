"""
Created on Mon Oct  9 20:35:21 2017

@author: hungngo
"""
import random
def generate_secret():
    a = random.randint(1, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    while(a==b or b==c or c==d or d==a or b==d or a==c):
        a = random.randint(1, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
    answer = str(a) + str(b) + str(c) + str(d)
    print(answer)
    return answer
    

def how_many_bulls(answer,guess):
    ''' Returns the number of bulls the guess earns when the secret number is answer. Both answer and guess should be strings'''

    bulls = 0
    for counter in range(len(answer)):
        if(answer[counter] == guess[counter]):
            bulls = bulls + 1
    return bulls

def how_many_cows(answer, guess):
    ''' Returns the number of bulls the guess earns when the
    secret number is answer. Both answer and guess should be strings'''
   
    cows_list = []
    bulls_list = []
    for s in range(len(answer)):
        for g in range(len(guess)):
            if(answer[s] == guess[g]):
		if(s == g):
                	bulls_list.append(guess[g])
		else:
			cows_list.append(guess[g])	

    final_set = set(cows_list) - set(bulls_list)

    return len(final_set)
