def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else print("Error, division by 0")

def calculator(): 
    print("\n\n--Python Calculator--")
    print("please choose:\n\n1. add\n2. subtract\n3. multipy\n4. divide\n5. Quit\n\n")

while True:
    calculator()
    try:
        choice = int(input("Your choice(1-5): "))
        if choice == 5: break
        else:
            operation = {1: add, 2: subtract, 3: multiply, 4: divide}
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
            print(f"Result: {operation[choice](n1, n2)}")
        
    except ValueError:
        print("please enter a valid number")