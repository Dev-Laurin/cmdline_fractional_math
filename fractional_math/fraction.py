import copy
import math 

class Fraction():
    def __init__(self, numerator, denominator, isMixed=False, wholenum=None):
        self.wholenum = wholenum
        self.numerator = int(numerator)

        if denominator == 0: 
            raise ZeroDivisionError("Fraction init cannot have 0 as a denominator.")

        self.denominator = int(denominator)
        self.isMixed = isMixed 

        if isMixed:
            self.numerator = int(denominator) * int(wholenum) + int(numerator)
            self.wholenum = None

    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / gcd 
        self.denominator = self.denominator / gcd 

    def prepareForAddOrSub(self, o):
        lhs = copy.deepcopy(self)
        rhs = copy.deepcopy(o) 
        
        lhs.denominator = self.denominator * o.denominator 
        lhs.numerator = self.numerator * o.denominator
        rhs.denominator = lhs.denominator
        rhs.numerator = o.numerator * self.denominator
        return [lhs, rhs]
        

    def __add__(self, o):
        res = self.prepareForAddOrSub(o)
        numerator = res[0].numerator + res[1].numerator 
        newNum = Fraction(numerator, res[1].denominator)
        newNum.reduce()
        return newNum

    def __mul__(self, o):
        numerator = self.numerator * o.numerator
        denominator = self.denominator * o.denominator
        newNum = Fraction(numerator=numerator, denominator=denominator)
        newNum.reduce()
        return newNum

    def __truediv__(self, o):
        temp = o.numerator
        numerator = o.denominator
        denominator = temp 

        if denominator == 0:
            raise ZeroDivisionError("Division Overloading: Fraction cannot have 0 as a denominator.")

        newNum = Fraction(numerator=numerator, denominator=denominator)

        return self * newNum 

    def __sub__(self, o):
        res = self.prepareForAddOrSub(o)

        numerator = res[0].numerator - res[1].numerator 
        newNum = Fraction(numerator=numerator, denominator=res[1].denominator)
        newNum.reduce()
        return newNum

    def convertToMixed(self):
        if self.wholenum is None:
            remainder = abs(int(self.numerator)) % int(self.denominator)
            self.wholenum = int(int(self.numerator) / int(self.denominator))
            self.numerator = remainder 

    def print(self):
        print(self.toString())

    def toString(self):
        if self.wholenum is not None or (abs(self.numerator) > self.denominator and self.denominator != 1):
            temp = copy.deepcopy(self)
            temp.convertToMixed()
            return str(int(temp.wholenum)) + "_" + str(int(temp.numerator)) + "/" + str(int(temp.denominator))
        elif self.denominator != 1:
            return str(int(self.numerator)) + "/" + str(int(self.denominator))
        else:
            return str(int(self.numerator))