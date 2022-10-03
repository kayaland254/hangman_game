#CREATING HANGMAN GAME
#TRIAL2

#1. Welcome message and generate random letter
#2. Ask user to guess letter
#3. Check if guessed letter is correct
#4. Check if array is complete.
#5. Check if player still has lives left.
#6. Combine logic

import random 

number_of_lives = 6
end_of_game = False


print("Welcome to the HANGMAN game!")
words_list = ["baboon", "camel", "blowfish", "orangutan", "lemar"]
random_word = random.choice(words_list)
random_word_length = len(random_word)
guessable_array = ["_"] * random_word_length

print (f"Psst. Your random letter is {random_word}.")
print (guessable_array)

while end_of_game == False: 
    guess = input("Please guess a letter.\n").lower()
    
    for position in range(random_word_length):
        letter = random_word[position]
        if guess == letter:
            guessable_array[position] = guess
    print(guessable_array)

    if guess not in random_word:
        number_of_lives -=1
        print(f"You have guessed a wrong letter. You have {number_of_lives} lives left.")

        if number_of_lives == 0:
            end_of_game = True
            print("You are out of lives. You lose.")

    if "_" not in guessable_array:
        end_of_game = True
        print(f"The word is {random_word}. You win!")



#TRIAL 1
# #1. Generate random letter
# import random
# guessable_words = ["camel", "aardvark", "baboon"]

# random_word = random.choice(guessable_words)
# print(random_word)

# #2. Set number of lives
# number_of_lives = 5

# #3. Generate blanks
# n = len(random_word)
# random_word_array = [" _ "] * n

# print(random_word_array)

# #4. Ask the user to guess a letter
# guess = input("Please guess a letter.\n").lower

# #5. Check if letter is right. If yes, add to array, if no deduct life.

# # for position in range(n):
# #     letter = random_word[position]

# #     if guess == letter:
# #         random_word_array[position] = letter
# #     else:
# #         new_number_of_lives = number_of_lives - 1
# # print (random_word_array)

# #6. Check if word is complete.
# complete_word = str(random_word_array)


# if complete_word == random_word:
#         print("You Win!")
# else:
#     while number_of_lives != 0:
#         for position in range(n):
                
#                 letter = random_word[position]

#                 if guess == letter:
#                     random_word_array[position] = letter
#                     print (random_word_array)
#                 else:
#                     number_of_lives -= 1
#     else:
#         print("You Lose.")
    
        


# # 7. Check if player still has enough lives to continue