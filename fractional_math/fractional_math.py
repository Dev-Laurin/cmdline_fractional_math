import sys 

def calculate(inputStr):
	output = inputStr
	print("= " + output)
	return 0

def main():
	print("Fractional calculator. Type quit to exit.")
	user_input = ""
	while(user_input != "quit"):
		user_input = input("? ")
		calculate(user_input)

if __name__ == '__main__':
    main()

