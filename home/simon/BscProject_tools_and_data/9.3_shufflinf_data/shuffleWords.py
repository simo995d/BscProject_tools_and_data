import sys, os, random

dataDir     = sys.argv[1] #original 1k or 10k directory
shuffledDir = sys.argv[2]; os.mkdir(shuffledDir) #path to wanted location of new shuffled directory

random.seed("42")

def firstCHAR1toCHAR2(string, char1, char2):
    flag = True
    newString = ""
    for char in string:
        if char == char1 and flag:    
            newString += char2
            flag = True
        else:
            newString += char
    return newString

def shuffleString(string):
    wasQ = False; wasDot = False; wasNewline = False

    if "?" in string:
        string = string.replace("?", "")
        wasQ = True
    if "." in string:
        string = string.replace(".", "")
        wasDot = True
    if "\n" in string:
        string = string.replace("\n", "")
        wasNewline = True
        
    stringList = string.split(' ')
    random.shuffle(stringList)
    shuffledString  = ' '.join(stringList)

    if wasQ:       shuffledString += "?"
    if wasDot:     shuffledString += "."
    if wasNewline: shuffledString += "\n"
    
    return shuffledString

for qa in os.listdir(dataDir):
    relPath = os.path.join(dataDir, qa)
       
    with open(relPath, 'r') as f:
        for line in f:
            rest = ""
            linetmp = line.split(" ", 1)
            ID = linetmp[0]
            linetmp = linetmp[1].split("\t", 1)
            text = linetmp[0]
            if len(linetmp) > 1: rest = "\t" +  linetmp[1]

            shufText = shuffleString(text)
            
            resLine = ID + " "  + shufText + rest
            with open(shuffledDir + "/" + qa, 'a') as new:
                new.write(resLine)
            


    

