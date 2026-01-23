"""
Loop examples
"""

def for_loop_demo():
    print("For loop counting 1 to 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print()

def while_loop_demo():
    print("While loop counting down from 5:")
    count = 5
    while count > 0:
        print(count, end=" ")
        count -= 1
    print()

def list_iteration():
    print("Iterating through a list:")
    colors = ["red", "green", "blue", "yellow"]
    for color in colors:
        print(f"- {color}")

if __name__ == "__main__":
    for_loop_demo()
    while_loop_demo()
    list_iteration()
