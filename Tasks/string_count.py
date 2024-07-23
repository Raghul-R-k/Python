def freq(word,letter):
    freq = 0
    for i in word:
        if i == letter :
            freq += 1
        return freq
def main():
    word = input('Enter the String : ')
    letter = input('Enter the letter to which frequency want to be find: ')
    print(f'Frequency of a letter {letter} in word {word}: ',freq(word,letter))
if __name__ == '__main__':
    main()
