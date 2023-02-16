import random
print("welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level =input("Choose a difficulty. Type easy' or hard':")
number= random.randint(1,100)
GAME_OVER = False
def easy (GAME_OVER,number):
    attempts = 10
    while(not GAME_OVER):
        print(f'YOu have {attempts} attempts remaining to guess the number.')
        guess =int(input('Make a Guess:'))
        if attempts == 0:
            GAME_OVER= True
        while(number != guess):
            attempts=attempts-1
            if(guess> number):
                print("Too High!")
                print("Guess Again")
                print(f'YOu have {attempts} attempts remaining to guess the number.')
                attempts=attempts-1
            elif(guess< number):
                print("Too low!")
                print("Guess Again")
                print(f'YOu have {attempts} attempts remaining to guess the number.')
                attempts=attempts-1
        if(number == guess):
            print('You got it.')
        
        
        

if level == "easy":
    easy(GAME_OVER,number)
