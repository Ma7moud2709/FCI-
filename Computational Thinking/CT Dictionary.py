print("1-Decomposition\n2-Pattern recognition\n3-Abstraction\n4-Algorithmic thinking\n5-Algorithm\n6-Program\n7-Computational thinking")
choice = int(input("Please enter the number of your choice from the following CT terms:"))

def dec(choice):
    switcher = {
        1: "Decomposition: Decomposition involves breaking down a large problem into smaller sub-problems",
        2: "Pattern recognition:",
        3:  "Abstraction: Abstraction involves removing unnecessary detail from a problem so that you can focus on the essentials",
        4:  "Algorithmic thinking:",
        5:  "Algorithm: Algorithm is a sequence of steps that can be followed to complete a task",
        6:  "Program: Program is an implementation of an algorithm",
        7:  "Computational thinking: CT is the thought processes involved in formulating a problem and expressing its solution(s) in such a way that a computer—human or machine—can effectively carry out",
    }
    return switcher.get(choice)
print(dec(choice))