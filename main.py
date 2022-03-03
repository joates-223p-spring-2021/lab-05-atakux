# -*- coding: utf-8 -*-
"""
Angela DeLeo
CPSC 223P-01
Wed Mar 02, 2022
atakux707@csu.fullerton.edu
"""

#import string library
import string

# This is the function that you must write the code for
def numWordsSpoken(candidate, word):
    """"This is a doc string that describes the function. Change it to your liking.
    Something like: This function returns the number of times a given word was 
    spoken by a given speaker"""

    if candidate in "OBAMA":
        return obamaSpeaks[word]
    elif candidate in "ROMNEY":
        return romneySpeaks[word]
    else:
        return 0


# This code will extract the data from the debate file and read it into one big
# string named debateString
debateFile = open("debate.txt", "r")
debateString = debateFile.read() 
debateFile.close()

# This code will extract the data from the stop words file and read it into one big
# string named stopWordsString
stopWordsFile = open("stopWords.txt", "r")
stopWordsString = stopWordsFile.read()
stopWordsFile.close()



#empty dictionaries
obamaSpeaks = {}
romneySpeaks = {}
lehrerSpeaks = {}

#empty lists
obamaLists = []
romneyLists = []

#initialize bools to false
obamaFound = False
romneyFound = False
lehrerFound = False


#function to add passed words to obamaSpeaks dict{}
def obamaDictAdd(w):
    #if the word was already found in the dictionary,
    #increase its count by 1
    if w in obamaSpeaks:
        obamaSpeaks[w] += 1
    #if the word wasnt found, set its count to 1
    else:
        obamaSpeaks[w] = 1

#function to add passed words to romneySpeaks dict{}
def romneyDictAdd(w):
    #if the word was already found in the dictionary,
    #increase its count by 1
    if w in romneySpeaks:
        romneySpeaks[w] += 1
    #if the word wasnt found, set its count to 1
    else:
        romneySpeaks[w] = 1

#function to add passed words to lehrerSpeaks dict{}
def lehrerDictAdd(w):
    #if the word was already found in the dictionary,
    #increase its count by 1
    if w in lehrerSpeaks:
            lehrerSpeaks[w] += 1
    #if the word wasnt found, set its count to 1
    else:
        lehrerSpeaks[w] = 1

#parsing thru the text and changing the bool values 
#depending on who is found to be speaking
for w in debateString.split():

    #obama was found to be speaking, so its bool is set
    #to true and all others are set to false
    if "OBAMA:" in w:
        obamaFound = True
        romneyFound = False
        lehrerFound = False 
        #keep parsing after we set obamas bool to true
        continue
    #romney was found to be speaking, so its bool is set
    #to true and all others are set to false
    elif "ROMNEY:" in w:
        obamaFound = False
        romneyFound = True
        lehrerFound = False
        #keep parsing after we set romneys bool to true
        continue
    #lehrer was found to be speaking, so its bool is set
    #to true and all others are set to false
    elif "LEHRER:" in w:
        obamaFound = False
        romneyFound = False
        lehrerFound = True
        #keep parsing after we set lehrers bool to true
        continue




    #disregard any extra wording around each speakers tag
    if w in "PRESIDENT BARACK":
        continue
    if w in "MR.":
        continue
    if w in "JIM":
        continue

    #convert to lowercase for more parsing
    w = w.lower()
    
    #remove punctuation
    w = w.strip(string.punctuation)

    #remove remaining punctuation that hasnt been removed
    w = w.replace('-', "")
    w = w.replace("'", "")

    #disregard any words that are in the stopWordsString
    if w in stopWordsString:
        continue




    #when obamas bool is true, obamas function is called
    #in order to add to its corresponding dictionary
    if obamaFound:
        obamaDictAdd(w)
    #when romneys bool is true, romneys function is called
    #in order to add to its corresponding dictionary
    if romneyFound:
        romneyDictAdd(w)
    #when lehrers bool is true, lehrers function is called
    #in order to add to its corresponding dictionary
    if lehrerFound:
        lehrerDictAdd(w)


    #end of word parsing



#apppend the dictionary items to each list in value, key order
#for printing and sorting purposes
for key, val in obamaSpeaks.items():
    obamaLists.append((val, key))
for key, val in romneySpeaks.items():
    romneyLists.append((val, key))



#sort and reverse the lists for printing purposes
obamaLists.sort(reverse=True)
romneyLists.sort(reverse=True)




#print obamas top 40 most used words
print("\nObama")
for i in range(40):
    print(f"{obamaLists[i][0]}:{obamaLists[i][1]}", end=" ")


#print romneys top 40 most used words
print("\n\nRomney")
for i in range(40):
    print(f"{romneyLists[i][0]}:{romneyLists[i][1]}", end=" ")
