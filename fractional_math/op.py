class Operator():
    def __init__(self, value):
        self.value = value 

    def __le__(self, o):
        if self.value in "*/+-" and o.value in "*/":
            return True 
        else:
            return False 

    def eval(self, num1, num2):
        if self.value == "*":
            return num1 * num2
        elif self.value == "/":
            return num1 / num2 
        elif self.value == "+":
            return num1 + num2 
        elif self.value == "-":
            return num1 - num2
        else:
            return None #unknown operator

    def print(self):
        print(self.value)