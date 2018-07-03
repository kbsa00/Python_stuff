
## SIMPLE FILE MANAGEMENT

def fileReadOperations():
    ##Reading a file 
    file = open("file.txt", "r"); 
    ##Printing the file
    print(file.read())
    ##Seek in the file
    file.seek(4)
    

    ##Printing the file information
    print("Name: ", file.name)
    print("Status: ", str(file.closed))
    print("Mode: ", file.mode)
    
    ##Reading the file each line by the time. 
    for line in file: 
        print(line)
    file.close()
    
   

def fileWriteOperations():
    ##For reading and writing
    ## Will create a new file if it does not exist
    file = open("write.txt", "w+")

    file.write("Hello file. I am string!")
    ## Seek for going back to the begining
    file.seek(0)
    print(file.read())
    file.close()


##Reading in to an array.
list = []
def fileTest(): 
    file = open('file.txt', 'r')
    for line in file: 
        list.append(line)
    file.close()


fileWriteOperations()
fileReadOperations()

fileTest()

