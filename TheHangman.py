import interface
import random

def get_word():
    file = open("palavras.txt", 'r')
    words = []
    for line in file:
        line = line.replace('\n','')
        words.append(line)
    file.close()
    n = random.randint(0,len(words)-1)
    return words[n]

def update(hidden, word, guess):
    new = ''
    for i in range(len(word)):
        letter = word[i]
        if letter == guess:
            new = new + letter
        else:
            new = new + hidden[i]
    return new

word = get_word()
hidden = '#'*len(word)
game = interface.hang(hidden)

while True:
    if game.guess() == True:
        guess = game.input()
        if guess in word:
            hidden = update(hidden, word, guess)
            game.right(hidden)
        else:
            game.wrong()
    game.update()
