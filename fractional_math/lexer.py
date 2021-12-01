from enum import Enum
from sys import prefix 
from .fraction import Fraction 
from .op import Operator 

class LEX(Enum):
    DIVIDE = 0
    MULT = 1
    SUB = 2
    ADD = 3
    MIXED = 4
    NUM = 5 
    OP = 6
    UNDERSCORE = 7

class STATE(Enum):
    START = -1 
    NUM = 0
    OP = 1 
    SPACE = 2 
    MIXED_NUM = 3
    END = 4 
    DIVIDE = 5 
    MULT = 6
    ADD = 7 
    SUB = 8 
    UNDEFINED = 100

def isNum(num):
    try: 
        float(num)
        return True 
    except ValueError:
        return False 

class Lexeme():
    def __init__(self, type, value, isMixed=False, numerator=None, denominator=None, fraction=None):
        self.TYPE = type 
        self.VAL = value 
        self.isMixed = isMixed

        if type == LEX.MIXED:
            self.VAL = Fraction(wholenum=value, isMixed=True, numerator=numerator, denominator=denominator)
        elif type == LEX.NUM:
            self.VAL = Fraction(value, 1)
        elif type == LEX.OP:
            self.VAL = Operator(value)

        if fraction is not None:
            self.VAL = fraction 

    def __repr__(self):
        return str(self.VAL)

    def __str__(self):
        return str(self.VAL)

    def print(self):
        self.VAL.print()

def Lex(string):
    #Extract into Lexemes 
    lexemes = []
    lexeme = ""
    i = 0 
    CURRENT_STATE = STATE.START
    PREV_STATE = CURRENT_STATE

    while i < len(string): 
        print("PREV_STATE: ", PREV_STATE)
        print("CURRENT_STATE ", CURRENT_STATE)
        char = string[i]
        print("char ", char)
        #Check if character can be converted to a number
        if isNum(char):
            lexeme += char
            PREV_STATE = CURRENT_STATE 
            CURRENT_STATE = STATE.NUM 

            if i + 1 < len(string):
                if string[i + 1] == "_":
                    #we have a mixed number 
                    PREV_STATE = CURRENT_STATE 
                    CURRENT_STATE = STATE.MIXED_NUM
                    #Find the numerator
                    j = i + 2
                    c = string[j]
                    numerator = ""
                    while c != "/":
                        numerator += c 
                        j += 1
                        c = string[j]
                        
                    #Find the denominator
                    j += 1
                    c = string[j]
                    denominator = ""
                    while j < len(string) and isNum(c):
                        c = string[j]
                        denominator += c 
                        j += 1
                                            
                    lexemes.append(Lexeme(LEX.MIXED, int(lexeme), numerator=numerator, 
                    isMixed=True, denominator=denominator))
                    lexeme = ""
                    lexemes[-1].print()
                    i = j - 1
            else:
                #end of string -- add the num
                print("NUM FOUND: " + str(lexeme))
                lexemes.append(Lexeme(LEX.NUM, int(lexeme)))

        else: 
            if CURRENT_STATE == STATE.NUM:
                #expression is a number --save 
                print("NUM FOUND: " + str(lexeme))
                lexemes.append(Lexeme(LEX.NUM, int(lexeme)))
                lexeme = ""
            
            if char in "*/+":
                #True OP
                lexemes.append(Lexeme(LEX.OP,char))  
                PREV_STATE = CURRENT_STATE 
                CURRENT_STATE = STATE.OP 
            elif char in "-" and CURRENT_STATE == STATE.SPACE and (PREV_STATE == STATE.NUM or PREV_STATE == STATE.MIXED_NUM):
                #True OP
                print("OP FOUND: -")
                lexemes.append(Lexeme(LEX.OP,char))  
                PREV_STATE = CURRENT_STATE 
                CURRENT_STATE = STATE.OP 
            elif char in "-" and (PREV_STATE == STATE.OP or PREV_STATE == STATE.START): 
                print("NEGATIVE NUM BEGIN")
                #Negative Num
                lexeme += char
                PREV_STATE = CURRENT_STATE 
                CURRENT_STATE = STATE.NUM 
            elif char == " ":
                #skip, no need to save 
                PREV_STATE = CURRENT_STATE
                CURRENT_STATE = STATE.SPACE 
            else: 
                raise ValueError("Invalid character in string.")
        i += 1 

    return lexemes