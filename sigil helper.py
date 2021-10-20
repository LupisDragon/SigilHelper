'''
This program is designed for aiding in creating sigils.

What it does: it will take a sentence that the user puts in, and will create two lists-
1) All the letters in the sentence, without repeat letters
2) All of the unique letters (only appearing once)
The program will then output both lists, and ask if there's another sentence needing to be
parsed.

Created by Ian Schwartz
'''

while True:
    letters = [] #all letters without repeats (list - for tracking purposes)
    sletters = '' #all letters without repeats (string - for display purposes)
    unique = '' #all unique letters (string)
    i = 0
    sigil = input("Please enter a sentence.\n")
    sigil = sigil.upper()
    while (i < len(sigil)):
        letter = sigil[i]
        if letter.isalpha():
            if letter not in letters:
                letters.append(letter)
                sletters += letter
            if sigil.count(letter) == 1:
                unique += letter
        i += 1
    #now we're done parsing the letters
    print ("\nHere are your letters without repeats.")
    print (sletters)
    print ("And these are the letters that are unique (only show up once).")
    print (unique)

    again = ''
    while (again != 'Y' and again != 'N'):
        again = input("\nWould you like to enter another sentence? (Y/N): ")
        again = again.upper()
        if (again != 'Y' and again != 'N'):
            print ("I'm sorry. I didn't get that. please try again.")
    if (again == "N"):
        break;
