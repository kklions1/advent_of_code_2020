def partOne(): 
    input = open("day3input.txt")
    
    data = []

    for line in input: 
        data.append(str(line.rstrip()))

    treeCount = 0
    row = 0
    col = 0

    maxRow = len(data)
    maxCol = len(data[0])

    while row < maxRow: 
        current = data[row][col]
        if current == '#':
            treeCount += 1
        
        row += 1
        col += 3
        if col >= maxCol:
            col = col % maxCol
        
    print(treeCount)


def partTwo():
    treeCount1 = treeCount(1, 1)
    treeCount2 = treeCount(1, 3)
    treeCount3 = treeCount(1, 5)
    treeCount4 = treeCount(1, 7)
    treeCount5 = treeCount(2, 1)

    print(treeCount1 * treeCount2 * treeCount3 * treeCount4 * treeCount5)

def treeCount(rowSlope, colSlope): 
    input = open("day3input.txt")
    
    data = []

    for line in input: 
        data.append(str(line.rstrip()))

    treeCount = 0
    row = 0
    col = 0

    maxRow = len(data)
    maxCol = len(data[0])

    while row < maxRow: 
        current = data[row][col]
        if current == '#':
            treeCount += 1
        
        row += rowSlope
        col += colSlope
        if col >= maxCol:
            col = col % maxCol
        
    return treeCount



if __name__ == "__main__": 
    partOne()
    partTwo()