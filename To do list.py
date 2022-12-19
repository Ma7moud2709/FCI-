my_list = []
completed = []
uncompleted = []

while True:

    print("1-Add a task.\n2-Delete a task\n3-Mark a task as complete.\n4-view tasks.\n5-Mark all as completed.\n"
          "6-Delete all tasks.")

    choice = str(input("-->"))
    # Add
    if choice == '1' or choice == "Add a task" :
        num = int(input("Enter number of tasks you want to add: "))

        for i in range(0, num):
            task = str(input("Enter a task to add: "))
            my_list.insert(len(my_list), task)
    # ---------------------------------------------------------------------------------
    # Delete
    elif choice == '2' or choice == "Delete a task":
        for i in range(0, len(my_list)):
            print(my_list.index(my_list[i]) + 1, "-", my_list[i], "\n")

        num = int(input("Enter number of tasks you want to delete: "))
        for i in range(0, len(my_list)):
            print(my_list.index(my_list[i]) + 1, "-", my_list[i], "\n")

        for i in range(0, num):
            task = int(input("\nEnter number of the task you want to delete: "))
            my_list.remove(my_list[my_list.index(my_list[task - 1])])
            print("Your new list:")
            for j in range(0, len(my_list)):
                print(my_list.index(my_list[j]) + 1, "-", my_list[j], "\n")
    # ---------------------------------------------------------------------------------
    # Mark as complete
    elif choice == '3' or choice == "Mark a task as complete":
        for i in range(0, len(my_list)):
            print(my_list.index(my_list[i]) + 1, "-", my_list[i], "\n")

        num = int(input("Enter number of tasks you want to mark as completed: "))

        for i in range(0, num):
            uncompleted = my_list.copy()
            task = int(input("\nEnter number of the task you want to mark as completed: "))
            completed.insert(len(completed), uncompleted[task - 1])
            print("Your uncompleted list:")
            for j in range(0, len(completed)):
                uncompleted.remove(uncompleted[task - 1])
            for j in range(0, len(uncompleted)):
                print(uncompleted.index(uncompleted[j]) + 1, "-", uncompleted[j], "\n")
    # ---------------------------------------------------------------------------------
    # View tasks
    elif choice == '4' or choice == "Mark a task as complete":
        print("1-All tasks.\n2-Completed tasks.\n3-Uncompleted tasks")
        view = str(input("Enter number of your choice: "))
        print("------------------------------------------------\n")
        # View all tasks.
        if view == '1' or view == "View all tasks":
            for i in range(0, len(my_list)):
                print(my_list.index(my_list[i]) + 1, "-", my_list[i], "\n")
                print("------------------------------------------------\n")
            print("|Total:", len(my_list), "|")
        # View completed tasks.
        if view == '2' or view == "View completed tasks":
            for j in range(0, len(completed)):
                print(completed.index(completed[j]) + 1, "-", completed[j], "\n")
                print("------------------------------------------------\n")
            print("|Total:", len(completed), "|")
        # View uncompleted tasks.
        if view == '3' or view == "View uncompleted tasks":
            for j in range(0, len(uncompleted)):
                print(uncompleted.index(uncompleted[j]) + 1, "-", uncompleted[j], "\n")
                print("------------------------------------------------\n")
            print("|Total:", len(uncompleted), "|")
    # ---------------------------------------------------------------------------------
    # Mark all as completed
    elif choice == 5 or choice == "Mark all as completed":
        completed = my_list.copy()
        uncompleted.clear()
    # ---------------------------------------------------------------------------------
    # Delete all
    elif choice == '6' or choice == "Delete all":
        my_list.clear()
        completed.clear()
        uncompleted.clear()
    # ---------------------------------------------------------------------------------
    # Ask to quit
    end = str(input("Another action?\n1-Yes\n2-No\n-->"))
    print("------------------------------")
    if end == '2' or end == "No":
        break