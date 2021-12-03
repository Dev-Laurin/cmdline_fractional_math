from enum import Enum
from sys import prefix 
from .fraction import Fraction 
from .op import Operator 

class LEX(Enum):
    MIXED = 0
    NUM = 1
    OP = 2

class STATE(Enum):
    START = 0 
    NUM = 1
    OP = 2
    SPACE = 3
    MIXED_NUM = 4

def is_num(num):
    try: 
        float(num)
        return True 
    except ValueError:
        return False 

class Lexeme():
    def __init__(self, type, value, is_mixed=False, numerator=None, denominator=None, fraction=None):
        self.TYPE = type 
        self.VAL = value 
        self.is_mixed = is_mixed

        if type == LEX.MIXED:
            self.VAL = Fraction(wholenum=value, is_mixed=True, numerator=numerator, denominator=denominator)
        elif type == LEX.NUM:
            self.VAL = Fraction(value, 1)
        elif type == LEX.OP:
            self.VAL = Operator(value)

        if fraction is not None:
            self.VAL = fraction 

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
        char = string[i]
        #Check if character can be converted to a number
        if is_num(char):
            lexeme += char

            if CURRENT_STATE != STATE.NUM:
                PREV_STATE = CURRENT_STATE 
                CURRENT_STATE = STATE.NUM 

            if i + 1 < len(string):
                if string[i + 1] == "_":
                    #we have a mixed number 
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
                    while j < len(string) and is_num(string[j]):
                        c = string[j]
                        denominator += c 
                        j += 1
                    lexemes.append(Lexeme(LEX.MIXED, int(lexeme), numerator=numerator, 
                    is_mixed=True, denominator=denominator))
                    lexeme = ""
                    i = j - 1
            else:
                #end of string -- add the num
                lexemes.append(Lexeme(LEX.NUM, int(lexeme)))

        else: 
            if CURRENT_STATE == STATE.NUM:
                #expression is a number --save 
                lexemes.append(Lexeme(LEX.NUM, int(lexeme)))
                lexeme = ""
            
            if char in "*/+":
                lexemes.append(Lexeme(LEX.OP,char))  
                PREV_STATE = CURRENT_STATE 
                CURRENT_STATE = STATE.OP 
            elif char in "-" and CURRENT_STATE == STATE.SPACE and (PREV_STATE == STATE.NUM or PREV_STATE == STATE.MIXED_NUM):
                lexemes.append(Lexeme(LEX.OP,char))  
                PREV_STATE = CURRENT_STATE 
                CURRENT_STATE = STATE.OP 
            elif char in "-" and (PREV_STATE == STATE.OP or PREV_STATE == STATE.START): 
                #Negative Num
                lexeme += char
                PREV_STATE = CURRENT_STATE 
                CURRENT_STATE = STATE.NUM 
            elif char == " ":
                #don't override previous state due to multiple spaces
                if CURRENT_STATE != STATE.SPACE:
                    PREV_STATE = CURRENT_STATE
                    CURRENT_STATE = STATE.SPACE 
            else: 
                raise ValueError("Invalid character in string '" + str(char) + "'")
        i += 1 

    return lexemes