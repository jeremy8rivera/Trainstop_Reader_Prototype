#Jeremy Rivera
#jr4222
#the purpose of the program is to take MTA system and
#list all stops for a specific train


#create clean file so easier to look at and work with
#Also allows for less messy code to work with
def createClean(filename, cleanFile):
    file = open(filename, 'r')
    cleaned = open(cleanFile, 'w')

    cleaned.write("stop_id, stop_name" + "\n")

    for line in file:
        file.readline()
        strippedFile = line.strip()
        splitFile = strippedFile.split(',')
        train_id = splitFile[0]
        endingofString = train_id[len(train_id)-1]
        
        
        if(train_id != "stop_id" and (endingofString != 'N') and (endingofString != 'S')):
            cleaned.write(splitFile[0] + ', ' + splitFile[2] + '\n')


    file.close()
    cleaned.close()


#Read New and Cleaned file
def cleanedReader(filename):
    stationDiction = {}
    
    file = open(filename, 'r')

    file.readline()

    for line in file:
        stripped = line.strip()
        splitFile = stripped.split(', ')
        string = str(splitFile[0])
        single = string[0]

        if single in stationDiction:
            stationDiction[single].append(splitFile[1])
        else:
            stationDiction[single] = [splitFile[1]]
                
    return stationDiction
        

#read through the dictionary to see if matches user request
def dictionReader(dictionary, request):
    for key, value in dictionary.items():
        if(key == request):
            listofValue = value
            return listofValue

#read the values from a key and create a string
def stringFromList(lst):
    string = ""
    for item in lst:
        string += item + ', '
    return string

#Handle all functions and user input
def main():
    createClean("train stop data-Windows.csv", "Train Stop Data Clean.csv")
    stationDiction = cleanedReader("Train Stop Data Clean.csv")

    done = False

    while(done == False):
        user_input = input("Please enter a train line, or 'done' to stop: ")
        if(user_input == 'done'):
            done = True
            
        else:
            try:
                lst = dictionReader(stationDiction, user_input)
                print(stringFromList(lst))
            except TypeError:
                print("That's not a valid option")
    

main()
