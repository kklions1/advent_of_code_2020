def partOne():
    input = open("day2input.txt")
    array = []
    for line in input: 
        array.append(str(line))
    
    validPasswordCount = 0

    for i in range(0, len(array)): 
        current = array[i].split(' ')
        count = current[0].split('-')
        minCount = int(count[0])
        maxCount = int(count[1])
        character = str(current[1][0:1])
        password = current[2]

        if password.count(character) >= minCount and password.count(character) <= maxCount: 
            validPasswordCount += 1

    print(validPasswordCount)
    return

def partTwo():
    input = open("day2input.txt")
    array = []
    for line in input: 
        array.append(str(line))
    
    validPasswordCount = 0

    for i in range(0, len(array)): 
        current = array[i].split(' ')
        index = current[0].split('-')
        firstIndex = int(index[0])
        secondIndex = int(index[1])
        character = str(current[1][0:1])
        password = current[2]
        if findInStringAtIndex(character, password, firstIndex - 1) and not findInStringAtIndex(character, password, secondIndex - 1):
            validPasswordCount += 1
        elif not findInStringAtIndex(character, password, firstIndex - 1) and findInStringAtIndex(character, password, secondIndex - 1):
            validPasswordCount += 1
        else: 
            pass
        
    print(validPasswordCount)
    return


def findInStringAtIndex(character, string, index):
    return string[index] == character


if __name__ == "__main__":
    partOne()
    partTwo()