def hangman():
    word = "EVAPORATE"
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    
    print("Welcome to Hangman!")
    print("Word to guess: " + word_completion)
    
    while not guessed:
        guess = input("Guess your letter: ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print("Incorrect!")
                guessed_letters.append(guess)
            else:
                print("Correct!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print("Incorrect!")
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input")
        
        print("Word to guess: " + word_completion)
    
    print(f"Congratulations! You've guessed the word {word} correctly!")

if __name__ == "__main__":
    hangman()
