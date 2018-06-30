import sys

def proccess (text):

    newWords = []

    for words in list(list(text[1:])):
        words = words + ' '
        charofword = list(words)

        for letter in charofword:
            if letter != ' ':
                newWords.append(':') #adds : to the end of the array
                newWords.append('regional_indicator_' + letter.lower())
                newWords.append(':'+' ')
            else:
                newWords.append(' '*3)


    sentence = "".join(newWords)
    return sentence

print (proccess(sys.argv))
