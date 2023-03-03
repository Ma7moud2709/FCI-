names = []
numbers = []
print("choose your action: \n1-Add.\n2-Remove.\n3-search.\n4-Show.\n5-remove all contacts.\n6-Quit.\n")

while True:
    choice = int(input("-->"))
    # Add
    if choice == 1:
        name = str(input("Enter contact 's name: "))
        names.insert(len(names), name)
        phone = str(input("Enter contact 's number: "))
        numbers.insert(len(numbers), phone)
    # Remove
    if choice == 2:
        name = str(input("Enter contact 's number: "))
        numbers.remove(numbers[names.index(str(name))])
        names.remove(name)
    # Search
    if choice == 3:
        name = str(input("Enter contact 's name: "))
        print(name, "\t", numbers[names.index(str(name))])
    # Show
    if choice == 4:
        if len(names) == 0:
            print("Empty!")
            continue
        for i in range(0, len(names)):
            print(i+1, "-", names[i], "\nPh:", numbers[i])

    # Clear
    if choice == 5:
        names.clear()
        numbers.clear()
    # Quit
    if choice == 6:
        break
