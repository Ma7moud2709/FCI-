while True:
    n1 = float(input("Num1= "))           # Get number 1
    n2 = float(input("Num2= "))           # Get number 2

    Process = int(input("Enter num of process:\n"       # Get process number
        "1-Add\n2-Sub\n3-Multi\n4-Division\n5-Modulus\n6-Power\n7-Sqrt\n"
          "-->"))

    # Division by 0 is undefined
    if n2 == 0 and Process == 3:
        print("Error")
    else:
        # Switcher to choose the process
        def calc(process):
            switcher = {
                # Add
                1: n1+n2,
                # Sub
                2: n1-n2,
                # Multi
                3: n1*n2,
                # Division
                4: n1/n2,
                # Modulus
                5: n1 % n2,
                # Power
                6: n1 ^ n2,
            }
            return switcher.get(Process)
        print("Result=", calc(Process), "\n")
        another = int(input("0-Quit the program\n1-Another operation\n-->"))
        if another == 0:
            break
