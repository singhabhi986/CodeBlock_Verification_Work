import re
import os
import shutil
#import fileinput



mapOfDefines = {} #Initializing empty dictionary as a table for defines.



#Is processing a .vh file of defines.
def readDefinedVariables(fileAddress):
    file = open(fileAddress,"r")
    fileLines = file.readlines()
    lineNo=1
    for line in fileLines:
        defineVariableObject = re.match(r'`define (.*?) (.*)',line)
        if defineVariableObject:
            mapOfDefines[defineVariableObject.group(1)] = defineVariableObject.group(2)
            #print("Variable: " + defineVariableObject.group(1) + " Value: " + defineVariableObject.group(2))
        #else:
            #print("Not Matched at LineNo: " + str(lineNo))
        #lineNo=lineNo+1






#will find address of each file that is to be processed
#One Argument
    #dirAddress that is to be processed
def processingEachFile(dirAddress):
    for dirPath, dirName, files in os.walk(dirAddress):
        for fileName in files:
            fileNameParts = fileName.split(".")
            if fileNameParts[-1] != "swp" and fileNameParts[-1] != "pdf":
                print(os.path.join(dirPath,fileName))
                processFile(str(os.path.join(dirPath,fileName)))






#Has two arguments
    #1- src: path to the source that is to be copied
    #2- dest: path to the destination(if destination folder is not created it will be formed) 
def makeACopyOfDirectory(src, dest):
    #Copy the content of Source to destination
    print('File Copied at: ' + dest)
    shutil.copytree(src,dest)



def processFile(pathToFile):
    f = open(pathToFile)

    stringList = f.readlines()
    f.close()
    count = 0
    print(stringList)
    for line in stringList:
        listOfDirectivesInLine = re.findall('`(\w+)', line)
        if len(listOfDirectivesInLine)>0:
            for directive in listOfDirectivesInLine:
                        if directive in mapOfDefines and mapOfDefines[directive]:
                            newLine = line.replace('`'+directive, mapOfDefines[directive])
                            print(newLine)
                            stringList[count] = newLine
                        else:
                            print("No defined for: " + directive)
        count = count+1
    print(stringList)
    f = open(pathToFile, 'w')
    newFileContents = "".join(stringList)
    f.write(newFileContents)
    f.close
    f = open(pathToFile)
    readFile = f.read()
    print(readFile)



def main():
    src = '../cha_swerv_11_testgenvar'#path to source
    dest = '../CopyOF_cha_swerv_11_testgenvar'#path to destination/CopyFolder
    makeACopyOfDirectory(src, dest)
    readDefinedVariables('../SweRV11_Source_and_DB/cha_swerv_11_testgenvar/configs/snapshots/128KB/common_defines.vh') #fileAddress as Argument
    processingEachFile(dest) #folderAddress as Argument





if __name__=="__main__":
    main()
