first_file = input("Enter the name of the file: ")
second_file = input("Enter the name of the second_file file: ")

first = open(first_file, 'r')
second = open(second_file, 'w')

data = first.read()
second.write(data)

print("Contents have been copied from the first file to the second file.")

first.close()
second.close()
