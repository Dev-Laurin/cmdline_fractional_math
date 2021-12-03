from .lexer import Lexeme, LEX, Lex

def calculateLexemes(num1, num2, op):
    return op.VAL.eval(num1.VAL, num2.VAL)

def printList(list, listname):
    print(listname, "[")
    for l in list:
        l.print()
    print("]")

def convert_to_reverse_polish_notation(lexemes):
    OUT = []
    OP = []

    op_count = 0 
    num_count = 0

    for lex in lexemes:
        if lex.TYPE == LEX.NUM or lex.TYPE == LEX.MIXED:
            OUT.append(lex)
            num_count += 1 
        elif lex.TYPE == LEX.OP:
            if len(OP) > 0 and lex.VAL <= OP[-1].VAL:
                OUT.append(OP[-1])
                OP.pop()
                OP.append(lex)
                op_count += 1 
            else:
                OP.append(lex)

    #end of lexemes, push all operators 
    for op in OP[::-1]:
        OUT.append(op)
        op_count += 1 

    if op_count + 1 != num_count:
        raise ValueError("Number of operators is not valid for the number of operands given.")

    return OUT

def calculate_reverse_polish_notation(stack):
    i = 0 
    while i < len(stack) and i >= 0 and len(stack) > 0:
        if stack[i].TYPE == LEX.OP:
            num = calculateLexemes(stack[i-2], stack[i-1], stack[i])
            stack.insert(i+1, Lexeme(LEX.NUM, 0, fraction=num))
            stack.pop(i)
            stack.pop(i-1)
            stack.pop(i-2)

            i = -1
        i += 1

    return stack[0]

def calculate(str):
    res = Lex(str)
    res = convert_to_reverse_polish_notation(res)
    res = calculate_reverse_polish_notation(res)
    return res.VAL 

def main():
    print("Fractional calculator. Type q to quit.")
    user_input = ""
    while(user_input != "q"):
        user_input = input("? ")
        try:
            print("= " + calculate(user_input).toString())
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except TypeError:
            print("Error: Invalid input. Must have operands and operators separated by spaces with the number of operators < number of operands.")
        except ValueError as e:
            if user_input != "q":
                print("Error:", e)

if __name__ == '__main__':
    main()