from .lexer import Lexeme, LEX, Lex

def calculateLexemes(num1, num2, op):
    return op.VAL.eval(num1.VAL, num2.VAL)

def convert_to_reverse_polish_notation(lexemes):
    OUT = []
    OP = []

    for lex in lexemes:
        if lex.TYPE == LEX.NUM or lex.TYPE == LEX.MIXED:
            OUT.append(lex)
        elif lex.TYPE == LEX.OP:
            if len(OP) > 0 and lex.VAL <= OP[-1].VAL:
                OUT.append(OP[-1])
                OP.pop(0)
                OP.append(lex)
            else:
                OP.append(lex)

    #end of lexemes, push all operators 
    for op in OP[::-1]:
        OUT.append(op)

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
	print("Fractional calculator. Type quit to exit.")
	user_input = ""
	while(user_input != "quit"):
		user_input = input("? ")
		try:
			print("= " + calculate(user_input).toString())
		except ZeroDivisionError:
			print("= " + "Error: Division by zero.")

if __name__ == '__main__':
    main()

