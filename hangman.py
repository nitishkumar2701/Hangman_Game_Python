import random
import hangman_stages
import wordList


randomWordList = []
blankList = []
remainingLives = 0

wordList = wordList.words
randomChoiceWord = random.choice(wordList)
randomChoiceWord = randomChoiceWord.lower()
blanksCount = len(randomChoiceWord)

for blankCount in range(blanksCount):
    blankList.append("_")

for letter in randomChoiceWord:
    randomWordList.append(letter)

print("Welcome to Hangman game ! \n")
print("Rules: \n Guess the word hiding behind the blanks ! \n You've got 6 lives \n These words are related to computer science \n Let's Begin \n ")
print(f"Find the {blanksCount} letter word related to computer science")
print(''.join(blankList))

while(remainingLives < 6 and "_" in blankList):
    userinputLetter = input("\n \nChoose a letter :")
    userinputLetter = userinputLetter.lower()
    if(userinputLetter in randomWordList):
        print("Keep Going Find the next letter")
        foundIndex = randomWordList.index(userinputLetter)
        blankList[foundIndex] = userinputLetter
        randomWordList[foundIndex] = "-"
        print(''.join(blankList))
    elif(userinputLetter not in randomWordList):
        remainingLives = remainingLives + 1
        print(f"Oops wrong guess, you have used {remainingLives} chance out of 6")
        print(hangman_stages.hangman_stages_list[remainingLives])
    else:
        print("Keep Going Find the next letter")
        print(''.join(blankList))

if(remainingLives == 6):
    print("\n Oops you failed to save the hangman , Game over :( \n")
    print(f" Word behind the blanks -> {randomChoiceWord} \n")
    print(hangman_stages.sad_ascii)
else:
    print("\n Great you won the game, you saved the hangman ! \n")
    print(hangman_stages.happy_ascii)

