def printAll(seq):
    print(f"seq: {seq}")
    if seq:
        print(seq[0])
        printAll(seq[1:])

printAll("This sentence tests this script.")
printAll((1,2,3,4,5))
