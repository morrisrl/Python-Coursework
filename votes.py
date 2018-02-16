import tools

while True:
    user_state = input("Which state's totals would you like to compute? (OR STOP): ")
    if user_state.lower() == "california":  #if the user input is california, we read the file
        california_file = open("california.txt", "r") #opens the file
        california_list = california_file.readlines() #reads the file
        california_file.close() #closes the file

    if user_state.lower() == "texas":
        texas_file = open("texas.txt", "r")  
        texas_list = texas_file.readlines()
        texas_file.close()
        
    if user_state.upper() == "STOP":  #stops the loop if user enters stop
        break

    if user_state == "california":
        stateList = california_list
    if user_state == "texas":
        stateList = texas_list

    largestVote = []
    votes = {}  #creates a dictionary of the villains
    for name in stateList:
        largestVote.append(name.strip().split("\t"))

    for name in largestVote:
        if name[0] in votes:
            votes[name[0]] += int(name[1])
        else:
            votes[name[0]] = int(name[1])

    texasList = list(votes.items())
    caliList = [texasList.pop()]

    while texasList:
        current = texasList.pop()

        for i in range(len(caliList)):
            if current[1] > caliList[i][1]:
                caliList.insert(i, current)
                current = ""
                break
        if current != "":
            caliList.append(current)

    tools.table_print(["Name", "Votes"], caliList, 15)
