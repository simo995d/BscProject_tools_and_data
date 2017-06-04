import sys, os
from subprocess import call

origDir = sys.argv[1] #path to 10k dataset
newDir  = sys.argv[2]; os.mkdir(newDir) #Wanted path for directory to be created
n = sys.argv[3] #number of training examples in the new directory    max 10k
qCount = 0

def countQuestions(qa):

    qCount = 0
    
    with open(qa, 'r') as f:
        for line in f:
            if line[-2].isalnum():
                qCount += 1
    return qCount

def countStories(qa):

    storyCount = 0
    
    with open(qa, 'r') as f:
        for line in f:
            if line[:2] == '1 ':
                storyCount += 1
    return storyCount


qas = os.listdir(origDir)

for qa in qas:
    questions = 0
    if ("qa3" in qa) or ("15" in qa) or ("16" in qa) or ("17" in qa) or ("19" in qa): #or True: ##Always true for all 20 tasks
        if qa.endswith("train.txt"):
            newqa  = open(os.path.join(newDir, qa), 'a')
            origqa = open(os.path.join(origDir, qa), 'r')
            for line in origqa:
                newqa.write(line)
                if line[-2].isalnum():
                    questions += 1
                    if questions == int(n): break

            newqa.close()
            origqa.close()
	
	if qa.endswith("test.txt"):
	    newqa  = open(os.path.join(newDir, qa), 'a')
            origqa = open(os.path.join(origDir, qa), 'r')
            for line in origqa:
                newqa.write(line)
                if line[-2].isalnum():
                    questions += 1
                    if questions == int(1000): break

            newqa.close()
            origqa.close()
       
         



