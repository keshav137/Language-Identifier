from dicts import DefaultDict

# Author: Keshav Malhotra, NETID: kmalhtr3

def bigrams(words):
    """Given an array of words, returns a dictionary of dictionaries,
    containing occurrence counts of bigrams."""
    d = DefaultDict(DefaultDict(0))
    for (w1, w2) in zip([None] + words, words + [None]):
        d[w1][w2] += 1
    return d

def wordDict(filename):
    file = open(filename, "r",encoding = "ISO-8859-1")
    wordDict = dict()
    readFile = file.read()
    lines = readFile.split('\n')
    for line in lines:
    	strings = line.split('\n')
    	for string in strings:
    		if string in wordDict:
    			wordDict[string] += 1
    		else:
    			wordDict[string] = 1
    return wordDict

def file2bigrams(filename):
    return bigrams(open(filename,encoding = "ISO-8859-1").read().split())

def main():
    #CHANGE THIS TO YOUR CURRENT WORKING DIRECTORY
    cwd = '/Users/keshavmalhotra/Desktop/406Assignment2/'

    outputPath = cwd + 'wordLangId.out'
    outputFile = open(outputPath, "w");


    englishFilePath = cwd + 'LangId.train.English'
    engWordCount = wordDict(englishFilePath)
    englishBigrams = file2bigrams(englishFilePath)

    frenchFilePath = cwd + 'LangId.train.French'
    frenchWordCount = wordDict(frenchFilePath)
    frenchBigrams = file2bigrams(frenchFilePath)

    italianFilePath = cwd + 'LangId.train.Italian'
    italianWordCount = wordDict(italianFilePath)
    italianBigrams = file2bigrams(italianFilePath)


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
        count += 1
        strings = sentence.split(' ')
        for i in range(len(strings) - 2):
            tup = (strings[i],strings[i + 1])

            #Adding one smoothing and calculating conditional probabilities
            if(tup[0] not in englishBigrams):
                englishBigrams[tup[0]] = dict();
            if(tup[1] not in englishBigrams[tup[0]]):
                englishBigrams[tup[0]][tup[1]] = 1;
            else:
                englishBigrams[tup[0]][tup[1]] += 1;
            if(tup[0] not in engWordCount):
                engWordCount[tup[0]] = 1
            else:
                engWordCount[tup[0]] += 1
            probEng = englishBigrams[tup[0]][tup[1]] / engWordCount[tup[0]]


            if(tup[0] not in frenchBigrams):
                frenchBigrams[tup[0]] = dict();
            if(tup[1] not in frenchBigrams[tup[0]]):
                frenchBigrams[tup[0]][tup[1]] = 1;
            else:
                frenchBigrams[tup[0]][tup[1]] += 1;
            if(tup[0] not in frenchWordCount):
                frenchWordCount[tup[0]] = 1
            else:
                frenchWordCount[tup[0]] += 1
            probFrench = frenchBigrams[tup[0]][tup[1]] / frenchWordCount[tup[0]]

            if(tup[0] not in italianBigrams):
                italianBigrams[tup[0]] = dict();
            if(tup[1] not in italianBigrams[tup[0]]):
                italianBigrams[tup[0]][tup[1]] = 1
            else:
                italianBigrams[tup[0]][tup[1]] += 1
            if(tup[0] not in italianWordCount):
                italianWordCount[tup[0]] = 1
            else:
                italianWordCount[tup[0]] += 1
            probItalian = italianBigrams[tup[0]][tup[1]] / italianWordCount[tup[0]]

            englishScore *= probEng
            frenchScore *= probFrench
            italianScore *= probItalian
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

    print("Accuracy of the word bigram model with one smoothing is:", str(round(accuracy / len(checkList) * 100 , 2)), "%")  




main()
