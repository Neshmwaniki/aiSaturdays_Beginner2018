import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

randomPhrase
def reverse(randomPhrase):
    if len(randomPhrase) == 0:
        return randomPhrase
    else:
        return reverse(randomPhrase[1:]) + randomPhrase[0]

print(reverse(randomPhrase))
