class Fraction (object):
    """
    A number represented as a fraction (numerator/denominator)
    """


    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom

    def __str__(self):
        """ Returns a string representation of self """
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        """Returns a new fraction after addition """
        top = self.num*other.denom + self.denom*other.num
        bottom = self.denom*other.denom
        return Fraction(top,bottom)

    def __sub__(self, other):
        """Returns a new fraction after substracion """
        top = self.num*other.denom - self.denom*other.num
        bottom = self.denom*other.denom
        return Fraction(top, bottom)
    
    def __float__(self):
        """Returns a float value of the fraction """
        return self.num/self.denom

    def inverse(self):
        """ Returns a new fraction representing  reverse of the numbers"""
        return Fraction(self.denom, self.num)
    
a = Fraction(1,4)
b = Fraction(3,4)
c = a + b #automatically c becomes a Fraction object

print(c) # internally calling built-in __str__() method of Fraction class
print(float(c)) # internally callling built-in __float__() methond of Fraction() class
print(Fraction.__float__(c))
print(float(b.inverse())) # internally calling custom reverse() method of Fraction class

# c = Fraction(3.14, 2.7) # assertion error
# print a*b # error, did not define ho to multiply two objects