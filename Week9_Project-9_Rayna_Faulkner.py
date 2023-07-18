def main():
    fileName = input("Enter the file name here: ")
    total = 0
    count = 0
    with open(fileName, 'r') as file:
        for line in file:
            for number in line.strip().split():
                total += float(number)
                count += 1
    print("\nThe average is " + str(total/count))
          
main()
