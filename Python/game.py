"""
Created on Mon Oct  9 20:37:24 2017

@author: hungngo
"""
import bulls_and_cows as bc

def main():
# Do not change this function!
    print('Welcome to Bulls and Cows death match!')
    again='y'
    while (again=='y'):
          play_game()
          again=input('would you like to play again? (y/n)')
    print('So long sucker!')

def play_game():
    ''' Plays one interactive game of bulls and cows on the console'''
    answer = str(bc.generate_secret())
    count = 0
    bulls = 0
    while(bulls < 4):
        guess = str(input('Take a guess '))
	print(guess)
        bulls = bc.how_many_bulls(answer,guess)
        cows = bc.how_many_cows(answer, guess)
        print ("You got", bulls, "bulls")
        print ("You got", cows, "cows")
        if (bulls < 4):
            print ("Take another guess")
        count = count + 1
    print ("Congratulations")
    print ("You have guessed", count, "times")



#call the main function to run the game
main()