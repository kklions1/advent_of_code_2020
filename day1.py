def partOne():
    input = open("day1Input.txt")

    array = []
    for line in input: 
        array.append(int(line))

    for i in range(0, len(array)): 
        for j in range(0, len(array)): 
            if array[i] + array[j] == 2020: 
                print(array[i] * array[j])
                return


def partTwo(): 
    input = open("day1Input.txt")

    array = []
    for line in input: 
        array.append(int(line))

    for i in range(0, len(array)): 
        for j in range(0, len(array)): 
            for k in range(0, len(array)): 
                if array[i] + array[j] + array[k] == 2020: 
                    print(array[i] * array[j] * array[k])
                    return


if __name__ == "__main__": 
    partOne()
    partTwo()