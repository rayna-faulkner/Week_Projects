fileName = input("Please enter the file name: ")
file = open(fileName, 'r', encoding='utf-8')
lineCount = 0

for line in file:
    lineCount = lineCount + 1

print("This file contains a linecount of: ", lineCount)

while True:
    lineNum = 0

    num = int(input("Please enter a line number or press 0 to quit: "))
    if num >=1 and num <= lineCount:
        file = open(fileName, 'r', encoding='utf-8')
        for lines in file:
            lineNum = lineNum + 1
            if lineNum == num:
                print(lines)
    else:
        if num == 0:
            print("Invalid number, exiting program.")
            break
