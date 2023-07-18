def median(list):
    sorted_list = sorted(list)
    midIndex = len(list) // 2
    if len(sorted_list) % 2 == 1:
        return sorted_list[midIndex]
    else:
        return (sorted_list[midIndex] + sorted_list[midIndex - 1]) / 2

def mean(list):
    total = 0
    for number in list:
        total += number
    return total / len(list)

def mode(list):
    numDictionary = {}
    for digit in list:
        numDictionary[digit] = numDictionary.get(digit, 0) + 1
    maxValue = max(numDictionary.values())
    modeList = []
    for key in numDictionary:
        if numDictionary[key] == maxValue:
            modeList.append(key)
    if len(modeList) == len(list):
        return 0
    else:
        return modeList[0]

# main function
def main():
    input_list = input("Enter a list of numbers: ")
    list = [int(num) for num in input_list.split()]
    print("List: ", list)
    print("Mode: ", mode(list))
    print("Median: ", median(list))
    print("Mean: ", mean(list))


main()
