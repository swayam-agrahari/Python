import random
# word=['apple','ball','beautiful']
import module
print(module.logo)
choosen_word = random.choice(module.word_list)
print(f'The choosen word is {choosen_word}')
display = []
for char in choosen_word:
    display += "_"
print(display)

end_of_game = False
lives = 6
while (not end_of_game):
    word = input("Enter a word: ").lower()
    if word in display:
        print(f"You 've already guessed {word}")
    for position in range(len(choosen_word)):
        if (word == choosen_word[position]):
            display[position] = word

    print(display)
    if '_' not in display:
        end_of_game = True
        print('You win')
    if word not in choosen_word:
        print(f'you have guessed {word}, thats not in  the word!!! You lose a life!')
        lives -=1
        if lives == 0:
            print("you lose")
            end_of_game=True
        
        print(module.stages[lives])
