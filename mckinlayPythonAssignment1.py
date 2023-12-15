import random
import re

#Function to create abbreviations
def create_abbreviation(sentence,userTextFile):
    #Remove special characters from sentence
    sentence = re.sub('[^A-Za-z0-9]+', ' ', sentence)
    #declartation of variables
    listOfAbbreviations = []
    abbreviationCounter = 0;
    abbreviation = ""
    possbileAbbreviations = 0;
    randomNumber1 = 0;
    randomNumber2= 0;
    outOfAbbreviations = False;
    randomNumberValid = False;
    wordsInSentence = sentence.split()
    numberOfWords = len(wordsInSentence)
    lenOfSentence = len(sentence)
    firstLetter = sentence[0]
    lowestScore = 100;
    abvOfLowestScore = ""
    letterToBeScored1 = ""

    #This generates every single possible abbreviation according to the rules
    while (outOfAbbreviations == False):
        randomNumber1 = random.randint(1,(lenOfSentence-1))
        randomNumber2 = random.randint(1,lenOfSentence)
        #generate a random number between 1 and the length of the sentence
        while (randomNumber2 >= randomNumber1):
            randomNumber1 = random.randint(1,(lenOfSentence-1))
            randomNumber2 = random.randint(1,lenOfSentence)
        else:
            
            randomNumberValid = True;
        #Basically gets the letter however many numbers away from the end and adds it to the abbreviation
        if (randomNumberValid == True):
            abbreviation += firstLetter
            
            
            abbreviation += sentence[-randomNumber1].upper()
            if not abbreviation == "":
                    if not any(not c.isalnum() for c in abbreviation):
                        letterToBeScored1 = sentence[-randomNumber1].upper()
                                   
        
            abbreviation += sentence[-randomNumber2].upper()
            if not abbreviation == "":
                    if not any(not c.isalnum() for c in abbreviation):
                        letterToBeScored2 = sentence[-randomNumber2].upper()
            #Makes sure only abbreviations that are three chars long are added to the list    
            acceptableAbreviation = len(abbreviation)
            if abbreviation in listOfAbbreviations:
                abbreviation = ""
                possbileAbbreviations += 1;
            if (possbileAbbreviations == 10000):
                outOfAbbreviations = True;
            #A bunch of checks to make sure only the acceptable abvs get added to list
            if not (abbreviation in listOfAbbreviations):
                if (acceptableAbreviation == 3):
                    if not ' ' in abbreviation:
                        if not abbreviation == "":
                            if not any(not c.isalnum() for c in abbreviation):
                                if not "   " in abbreviation:
                                    #add valid abbraviation to the list of abbreviations
                                    listOfAbbreviations.append(abbreviation)
                                    print("The abbreviation is: " + abbreviation)
                                    scoreOf1stLetter = score_abbreviations(letterToBeScored1, sentence, randomNumber1, wordsInSentence, numberOfWords)
                                    scoreOf2ndLetter = score_abbreviations(letterToBeScored2, sentence, randomNumber2, wordsInSentence, numberOfWords)
                                    totalScore = scoreOf1stLetter + scoreOf2ndLetter
                                    print ("The total score is: "+ str(totalScore))
                                    print(abbreviation + "  " + str(totalScore))
                                    #Update the lowest score
                                    if totalScore < lowestScore:
                                        lowestScore = totalScore
                                        abvOfLowestScore = abbreviation
                                        print ("New lowest score is: " + str(lowestScore) + " for abbreviation " + abvOfLowestScore)
                                    #Reset the abbreviation for next loop    
                                    abbreviation = ""
                                    randomNumberValid = False
            if (acceptableAbreviation > 3):
                abbreviation = ""
                randomNumberValid = False
    print("The lowest scoring abbreviation was " + abvOfLowestScore + " with a score of " + str(lowestScore))
    #After all abbreviations have been generated and the lowest score has been found, call the write to file function
    writeToFile(userTextFile, sentence, abvOfLowestScore)
                
      
    

def score_abbreviations(letterToBeScored, sentence, randomNumber, wordsInSentence, numberOfWords):
    #Declaration of variables
    positionOfLetter = 0;
    scoreCounter = 0;
    numberOfSpaces = 0;
    wordCounter = 1;
    loopCounter = 0
    lengthOfSentence = (len(wordsInSentence))
    lengthOfFullSentence = (len(sentence))
    
    #Lists for all the different potential scores
    listOf1Score = ['Q','Z']
    listOf3Score = ['J','X']
    listOf6Score = ['K']
    listOf7Score = ['F','H','V','W','Y']
    listOf8Score = ['B','C','M','P']
    listOf9Score = ['D','G']
    listOf15Score = ['L','N','R','S','T']
    listOf20Score = ['O','U']
    listOf25Score = ['A','I']
    listOf35Score = ['E']
    shouldBeScored = True
    print("The letter to be score: " + letterToBeScored)
    print("The number passed in: " +str(randomNumber))

    
    
    #Calculate position of letters in word in regards to sentence
    positionOfLetter = lengthOfFullSentence - randomNumber;
    print("The position of the letter is: " + str(positionOfLetter))
    
    #Scoring system based on the rules set out by the document
    if (numberOfWords > 1):
        print (sentence)
        firstLetters = [s[0] for s in sentence.split()]
        if letterToBeScored in firstLetters:
            scoreCounter += 0
            shouldBeScored = False;
            return scoreCounter
        
    #Generates score based on where the letter was positioned in the sentence
    if (positionOfLetter == 0):
        scoreCounter = 0;
        return scoreCounter
    if (positionOfLetter == (lengthOfFullSentence-1)):
        if (letterToBeScored == "E"):
            scoreCounter += 20
            return scoreCounter
        else:
            scoreCounter += 5
            return scoreCounter
        
    if not ((positionOfLetter == 0) & (positionOfLetter == -1)):
        if (positionOfLetter == 1):
            scoreCounter += 1
            
        if (positionOfLetter == 2):
            scoreCounter += 2
            
        if ((positionOfLetter != 1)):
            if ((positionOfLetter !=2)):
                scoreCounter += 3
                
           #All the different scores for the different letters
        if letterToBeScored in listOf1Score:
            scoreCounter += 1
        if letterToBeScored in listOf3Score:
            scoreCounter += 3
        if letterToBeScored in listOf6Score:
            scoreCounter += 6
        if letterToBeScored in listOf7Score:
            scoreCounter += 7
        if letterToBeScored in listOf8Score:
            scoreCounter += 8
        if letterToBeScored in listOf9Score:
            scoreCounter += 9
        if letterToBeScored in listOf15Score:
            scoreCounter += 15
        if letterToBeScored in listOf20Score:
            scoreCounter += 20
        if letterToBeScored in listOf25Score:
            scoreCounter += 25
        if letterToBeScored in listOf35Score:
            scoreCounter += 35
            
    print ("The score counter is " + str(scoreCounter))
    return scoreCounter
    
def writeToFile(userTextFile, sentence, abvOfLowestScore):
    outputFile = "Mckinlay_"+userTextFile+"_"+"abbrevs.txt"
    f = open(outputFile, "a")
    f.writelines([sentence + "\n",abvOfLowestScore + "\n"])
    f.close()
    

def main():
    lines = []
    counter = 0
    userTextFile = input("Enter Text File\n")
    textFile = userTextFile + ".txt"
    #Open the text file provided by user and read the lines into a list. If that is unsuccessful, display error message and close program
    try:
        with open(textFile) as f:
            lines = f.read().splitlines()
            listOfAbbreviations = [None] * len(lines)
    except FileNotFoundError:
        print("file does not exist\n")
        exit([1])
        #for each line call the create_abbreviation function
    for i in lines:
        abbreviationResult = create_abbreviation(lines[counter],userTextFile)
        counter += 1
    
    

main()


