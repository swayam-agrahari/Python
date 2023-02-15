import random
print("welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level =input("Choose a difficulty. Type easy' or hard':")
number= random.randint(1,100)
GAME_OVER = False
while(not GAME_OVER):
    def easy ():
        attempts = 10
        print(f'YOu have {attempts} attempts remaining to guess the number.')
        guess =input('Make a Guess:')
        if attempts == 0:
            GAME_OVER= True
        while(number != guess):
            attempts=attempts-1
            if(guess> number):
                print("Too High!")
                print("Guess Again")
                print(f'YOu have {attempts} attempts remaining to guess the number.')
            elif(guess< number):
                print("Too low!")
                print("Guess Again")
                print(f'YOu have {attempts} attempts remaining to guess the number.')
        if(number == guess):
            print('You got it.')
        
        

if level == "easy":
    easy()
