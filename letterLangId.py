
# Author: Keshav Malhotra, NETID: kmalhtr3

#function returns a list of all the bigrams contained in the input file
def letterBigramList(filePath):
    file = open(filePath, "r",encoding = "ISO-8859-1")
    bigramList = []  #list containing bigrams
    readFile = file.read()
    lines = readFile.split('\n')
    for line in lines:
        strings = line.split(' ')
        for string in strings:
            for x in range(len(string)):
                n = string[x:x + 2]
                if len(n) == 2:
                    bigramList.append(n)
    file.close()
    return bigramList

#Returns a dictionary containing the character as keys and their frequencies as values, in the given file
def charCount(filePath):
    file = open(filePath, "r",encoding = "ISO-8859-1")
    charDict = dict()
    readFile = file.read()
    lines = readFile.split('\n')
    for line in lines:
        strings = line.split(' ')
        for string in strings:
            for x in range(len(string)):
                if string[x] in charDict:
                    charDict[string[x]] += 1
                else:
                    charDict[string[x]] = 1
    file.close()
    return charDict


def main():
    
    #CHANGE THIS TO YOUR CURRENT WORKING DIRECTORY
    cwd = '/Users/keshavmalhotra/Desktop/406Assignment2/'

    outputPath = cwd + 'letterLangId.out'
    #opening output file 
    outputFile = open(outputPath, "w");

    englishFilePath = cwd + 'LangId.train.English'
    englishBigrams = letterBigramList(englishFilePath)
    englishBigramDict = dict()
    engCharCount = charCount(englishFilePath)

    #Initializing englishBigramDict, contians bigram as key and frequency as value
    for bigram in englishBigrams:
        if bigram in englishBigramDict:
            englishBigramDict[bigram] += 1
        else:
            englishBigramDict[bigram] = 1



    frenchFilePath = cwd + 'LangId.train.French'
    frenchBigrams = letterBigramList(frenchFilePath)
    frenchBigramDict = dict()
    frenchCharCount = charCount(frenchFilePath)

    #Initializing frenchBigramDict, contians bigram as key and frequency as value
    for bigram in frenchBigrams:
        if bigram in frenchBigramDict:
            frenchBigramDict[bigram] += 1
        else:
            frenchBigramDict[bigram] = 1


    italianFilePath = cwd + 'LangId.train.Italian'
    italianBigrams = letterBigramList(italianFilePath)
    italianBigramDict = dict()
    itCharCount = charCount(italianFilePath)

    #Initializing italianBigramDict, contians bigram as key and frequency as value
    for bigram in italianBigrams:
        if bigram in italianBigramDict:
            italianBigramDict[bigram] += 1
        else:
            italianBigramDict[bigram] = 1



    testFilePath = cwd + 'LangId.test'
    testFile = open(testFilePath,encoding = "ISO-8859-1").read()


    checkFilePath = cwd + 'LangId.sol'
    checkFile = open(checkFilePath,encoding = "ISO-8859-1").read()


    testList = testFile.split('\n')
    checkList = checkFile.split('\n')

    count = 0

    for sentence in testList:
        englishScore = 1
        italianScore = 1
        frenchScore = 1
        strings = sentence.split(' ')
        count = count + 1
        for string in strings:
            for x in range(len(string)):
                n = string[x:x + 2] # getting a bigram from a string in a sentence
                if len(n) != 2:
                    continue
                first = n[0]
                engProb = 0
                italianProb = 0
                frenchProb = 0

                #calculating condiitonal probabilities
                if n in englishBigramDict and first in engCharCount:
                    engProb = englishBigramDict[n] / engCharCount[first]

                if n in frenchBigramDict and first in frenchCharCount:
                    frenchProb = frenchBigramDict[n] / frenchCharCount[first]

                if n in italianBigramDict and first in itCharCount:
                    italianProb = italianBigramDict[n] / itCharCount[first]

                #taking product of all conditional probabilities
                englishScore *= engProb   
                italianScore *= italianProb 
                frenchScore *= frenchProb   
        if count == 301: #ignoring the last blank value
            continue
        elif(max(englishScore,frenchScore,italianScore) == englishScore):
            outputFile.write(str(count) + " English\n")
        elif(max(englishScore,frenchScore,italianScore) == italianScore):
            outputFile.write(str(count) + " Italian\n")
        else:
            outputFile.write(str(count) + " French\n")  
        


    outputFile.close()

    accuracy = 0
    outputFile = open(outputPath,encoding = "ISO-8859-1").read()
    outputList = outputFile.split('\n')
    for i in range(len(checkList)):
        if checkList[i] == outputList[i]:
            accuracy = accuracy + 1


    print("Accuracy of the letter bigram model is:", str(round(accuracy / len(checkList) * 100 , 2)), "%")

main()

