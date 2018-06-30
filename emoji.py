import sys #neccessary for sys.argv

def proccess (text):

    newWords = [] #initialises aray that will hold the modified letters

    for words in list(list(text[1:])): #ARRAYS START AT 1 REEEEE. Jokes. This is used as the name of the program is normaly also taken in as an argument. This is to stop that being sent as input.

        words = words + ' ' #Adds space at the end of the words so that there is a space when you copy over

        charofword = list(words) #Creates a character array

        for letter in charofword: #Itterates for every character in the charofword array (including space.)
            if letter != ' ': #This is to stop spaces being modified.
                newWords.append(':') #Adds : to the end of the array
                newWords.append('regional_indicator_' + letter.lower())
                newWords.append(':'+' ') #Neccesary as discord has a spaz if u dont add a space.
            else:
                newWords.append(' '*3) #Makes spaces larger to make them actually visible


    sentence = "".join(newWords) #Makes the newWords array a string.
    return sentence #returns the value

print (proccess(sys.argv)) #"sys.argv" takes arguments from the command line it is then taken as the variable text.

#this is a test for push.
