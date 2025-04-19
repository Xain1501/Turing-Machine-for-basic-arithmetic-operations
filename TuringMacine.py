def unary_subtract_tm(a, b, show=True):
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

    remaining = [i for i in tape if i == 1]
    result = len(remaining)
    if show:
        print("Subtraction Result (Decimal):", result)
        print("-" * 40)
    return result

def unary_division_tm(a, b):
    if b == 0:
        print("Error: Division by zero.")
        return
    
    print(f"\nPerforming Division: {a} ÷ {b}")
    print("=" * 40)
    quotient = 0

    while a >= b:
        a = unary_subtract_tm(a, b)
        quotient += 1

    print(f"Final Quotient: {quotient}")
    print(f"Final Remainder: {a}")

def main():
    print("Unary Division Turing Machine")
    try:
        a = int(input("Enter dividend (a): "))
        b = int(input("Enter divisor (b): "))
        unary_division_tm(a, b)
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
