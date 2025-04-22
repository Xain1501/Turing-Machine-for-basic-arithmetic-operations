def get_inputs():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    return a, b

def add():
    a, b = get_inputs()
    tape = ['1'] * a + ['+'] + ['1'] * b + ['_']
    while '+' in tape:
        head = tape.index('+')
        tape[head] = '1'
        while tape[head] != '_':
            head += 1
        head -= 1
        while tape[head] != '1':
            head -= 1
        tape[head] = '_'
    return tape.count('1')

def unaryMultiplication():
    a, b = get_inputs()
    tape = ['1'] * a + ['*'] + ['1'] * b + ['_'] * (a * b)
    starPos = tape.index('*')
    multiplicandCount = tape[:starPos].count('1')
    multiplierStart = starPos + 1
    multiplierEnd = len(tape)
    while multiplierEnd > multiplierStart and tape[multiplierEnd - 1] != '1':
        multiplierEnd -= 1
    writeHead = len(tape) - 1
    while tape[writeHead] == '_':
        writeHead -= 1
    writeHead += 1
    for _ in range(multiplicandCount):
        for i in range(multiplierStart, multiplierEnd):
            if tape[i] == '1':
                tape[writeHead] = 'X'
                writeHead += 1
    return tape.count('X')

def Subtract(show=True):
    a, b = get_inputs()
    if a < b:
        print("Cannot perform subtraction when a < b")
        return None
    tape = [1] * a + [-1] + [1] * b
    head = 0
    if show:
        print("Subtraction Step - Initial Tape:", tape)
    while head < len(tape):
        if tape[head] == 1:
            search = head
            while search < len(tape) and tape[search] != -1:
                search += 1
            search += 1
            while search < len(tape):
                if tape[search] == 1:
                    tape[head] = 'X'
                    tape[search] = 'X'
                    if show:
                        print("Updated Tape:", tape)
                    break
                search += 1
        head += 1
    result = tape.count(1)
    if show:
        print("Subtraction Result (Decimal):", result)
        print("-" * 40)
    return result

def Divide():
    print("Prompt a as the numerator and b as the denominator")
    a, b = get_inputs()
    if b == 0:
        print("Error: Division by zero.")
        return
    print(f"\nPerforming Division: {a} ÷ {b}")
    print("=" * 40)
    quotient = 0
    while a >= b:
        a = a - b
        quotient += 1
    print(f"Final Quotient: {quotient}")
    print(f"Final Remainder: {a}")

def power():
    print("Prompt a as the base and b as the exponent")
    a = int(input("Enter base: "))
    b = int(input("Enter exponent: "))
    res = 1
    for _ in range(b):
        res = unaryMultiplication_single(res, a)
    return res

def unaryMultiplication_single(a, b):
    # helper version used for chaining (to avoid double input())
    tape = ['1'] * a + ['*'] + ['1'] * b + ['_'] * (a * b)
    starPos = tape.index('*')
    multiplicandCount = tape[:starPos].count('1')
    multiplierStart = starPos + 1
    multiplierEnd = len(tape)
    while multiplierEnd > multiplierStart and tape[multiplierEnd - 1] != '1':
        multiplierEnd -= 1
    writeHead = len(tape) - 1
    while tape[writeHead] == '_':
        writeHead -= 1
    writeHead += 1
    for _ in range(multiplicandCount):
        for i in range(multiplierStart, multiplierEnd):
            if tape[i] == '1':
                tape[writeHead] = 'X'
                writeHead += 1
    return tape.count('X')

def main():
    print("Unary Turing Machine for Arithmetic Operations:")
    while True:
        print("\nChoose an option:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Power")
        print("6: Exit")

        choice = input("Enter choice (1 to 6): ")
        if choice == '6':
            print("Exiting!")
            break
        elif choice == '1':
            result = add()
            print("Result:", result)
        elif choice == '2':
            result = Subtract()
            if result is not None:
                print("Result:", result)
        elif choice == '3':
            result = unaryMultiplication()
            print("Result:", result)
        elif choice == '4':
            Divide()
        elif choice == '5':
            result = power()
            print("Result:", result)
        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()
