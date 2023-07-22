import random

hangman = [
    '''
    ________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___ ''',
    '''
        _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H ''',
    '''
         _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA''',
    '''
        ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN''',
    '''
        _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG''',
    '''
        _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM''',
    '''
        ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA''',
    '''
         ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN'''
]

print("This is a Hollywood Movie Hangman Game\n")
print('''   
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
''')
print("RULES:\n1. The movie will be randomly chosen by the system, and an appropriate clue will be provided.")
print("2. You are allowed to enter only one letter at a time.")
print("3. You have 7 lives before the game is over.\n")

choosen_list = ['Inception', 'Blade Runner', 'Apocalypse Now', 'Seven Samurai', 'A Clockwork Orange']
word = list(random.choice(choosen_list))
wordf = ''.join(word)

final_word = ''.join(word).lower()  # Converts list to string, making all the letters lowercase
final_word_list = list(final_word)  # Creates a list of each of the lowercase list items

final_underscore_list = final_word_list[:]
for l in range(len(final_underscore_list)):
    if final_underscore_list[l].isalpha():
        final_underscore_list[l] = '_'

clue = ''
if wordf == choosen_list[0]:
    clue = 'A mind-bending movie directed by Christopher Nolan, where the characters enter dreams within dreams to steal secrets.'
elif wordf== choosen_list[1]:
    clue = 'A sci-fi movie set in a dystopian future, directed by Ridley Scott, where a detective hunts down artificial beings known as "replicants."'
elif wordf== choosen_list[2]:
    clue = 'A war movie directed by Francis Ford Coppola, loosely based on Joseph Conrad\'s "Heart of Darkness."'
elif wordf== choosen_list[3]:
    clue = 'A Japanese epic, directed by Akira Kurosawa, about a group of samurai defending a village from bandits.'
elif wordf== choosen_list[4]:
    clue = 'A dystopian film directed by Stanley Kubrick, based on Anthony Burgess\'s novel, exploring themes of free will and violence.'

print(f"Guess the movie: {' '.join(final_underscore_list)}")
print(f"\n Clue: {clue}\n")
print(f"You're at level- {hangman[0]}")
print("You have 7 lives")


wrong = 1
while ''.join(final_underscore_list) != final_word and wrong <= 7:
    user_choice = input("Enter a letter to make a guess -> ").lower()

    if len(user_choice) != 1 or not user_choice.isalpha():
        print("Please enter a single letter.")
        continue

    if user_choice not in final_word_list:
        print(f"{hangman[wrong]}")
        wrong += 1
    else:
        for i in range(len(final_underscore_list)):
            if user_choice == final_word_list[i]:
                final_underscore_list[i] = user_choice
        print(' '.join(final_underscore_list))
        print("\n")
    

if ''.join(final_underscore_list) == final_word:
    print("Congratulations, you have won the game!")
else:
    print(f"Sorry, you lost! \nThe Movie was: {final_word}. Better luck next time!")


    
    
  
  