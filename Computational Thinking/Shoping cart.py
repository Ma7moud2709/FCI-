cart = []
print("choose your action: \n1-Add.\n2-Remove.\n3-Clear\n4-Show.\n5-Quit\n")

while True:
    choice = int(input("-->"))
    if choice == 1:
        element = str(input("Enter the element: "))
        cart.insert(len(cart), element)
    if choice == 2:
        element = str(input("Enter the element: "))
        cart.remove(element)
    if choice == 3:
        cart.clear()
    if choice == 4:
        print(cart)
    if choice == 5:
        break
