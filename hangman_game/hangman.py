import random
#word=['apple','ball','beautiful']
import module
choosen_word= random.choice(module.word_list)
print(f'The choosen word is {choosen_word}')
display = []
for char in choosen_word:
    display+= "_"
print(display)

end_of_game= False
while(not end_of_game):
    word=input("Enter a word: ").lower() 
    for position in range(len(choosen_word)):
        if(word == choosen_word[position]):
            display[position]= word
    print(display)
    if '_' not in display:
        end_of_game= True
        print('You win')

