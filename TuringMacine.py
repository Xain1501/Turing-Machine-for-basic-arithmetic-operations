def Subtract(a, b, show=True):
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

def Divide(a, b):
    if b == 0:
        print("Error: Division by zero.")
        return
    
    print(f"\nPerforming Division: {a} ÷ {b}")
    print("=" * 40)
    quotient = 0

    while a >= b:
        a = Sub(a, b)
        quotient += 1

    print(f"Final Quotient: {quotient}")
    print(f"Final Remainder: {a}")

def power(a,b):
    res=1;
    for _ in range(b):
        res=multiply(res,a)
        
    return res

def main():
    print("unary turing machine for Arithmetic Operations: ")
    
    while True:
        print("choose an option: ")
        print("1: Add ")
        print("2: Subtract ")
        print("3: Multiply ")
        print("4: Divide ")
        print("5: Power ")
        print("6: Exit ")
        
        choice = input("enter choice 1 to 6: ")
        if choice=='6':
            print("exiting! ")
            break
        
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        
        if choice =='1':
            add(a,b)
            
        elif choice =='2':
            if a<b:
                printf("can not perforn subtract when a<b")
                break
            else:
                Subtract(a,b)
        
        elif choice =='3':
            multiply(a,b)
        
        
        elif choice =='4':
            Divide(a,b)
            
        
        elif choice =='5':
            power(a,b)
        
        
        else:
            printf("invalid option selected!")
            
        



