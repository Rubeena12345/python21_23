newFile = open("trial.txt","a")
newFile.write("ADDED NEW TEXT \n")
newFile.close()
readFile = open("trial.txt","r")
print(readFile.readlines())
readFile.close()
