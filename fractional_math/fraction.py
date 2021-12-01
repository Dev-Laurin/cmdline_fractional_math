import copy 

def get_gcd(num1, num2): #30, 8
    num1 = int(num1)
    num2 = int(num2)
    smallestNum = min(num1, num2)
    factor = 0
    for i in range(1, smallestNum + 1):
        if smallestNum % i == 0 and num2 % i == 0:
            factor = i 

    return factor 

class Fraction():
    def __init__(self, numerator, denominator, isMixed=False, wholenum=None):
        self.wholenum = wholenum
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.isMixed = isMixed 

        if isMixed:
            self.numerator = int(denominator) * int(wholenum) + int(numerator)
            self.wholenum = None

    def reduce(self):
        #gcd = get_gcd(self.numerator, self.denominator)
        import math 
        gcd = math.gcd(self.numerator, self.denominator)
        print("GCD", gcd)
        self.numerator = self.numerator / gcd 
        self.denominator = self.denominator / gcd 


    def prepareForAddOrSub(self, o):
        print("preparing for addition")
        lhs = copy.deepcopy(self)
        rhs = copy.deepcopy(o) 
        
        lhs.denominator = self.denominator * o.denominator 
        print("new denominator", lhs.denominator)
        lhs.numerator = self.numerator * o.denominator
        rhs.denominator = lhs.denominator
        print(rhs.numerator, rhs.denominator, rhs.wholenum)
        print(self.denominator)
        rhs.numerator = o.numerator * self.denominator
        print("new numerator [lhs, rhs]", lhs.numerator, rhs.numerator)
        return [lhs, rhs]
        

    def __add__(self, o):
        res = self.prepareForAddOrSub(o)
        numerator = res[0].numerator + res[1].numerator 
        print("Added nume", numerator)
        print("new deno", res[1].denominator)
        newNum = Fraction(numerator, res[1].denominator)
        newNum.reduce()
        print(newNum.numerator, newNum.denominator)
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