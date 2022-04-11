import math

class Complex(object):
    def __init__(self, real, imaginary):
       self.real = real
       self.imaginary = imaginary
        
    def __add__(self, no):
        a = self.real + no.real
        b = self.imaginary + no.imaginary
        return Complex(a, b)
    
    def __sub__(self, no):
        a = self.real - no.real
        b = self.imaginary - no.imaginary
        return Complex(a, b)
    
    def __mul__(self, no):
        a = self.real*no.real
        b = self.imaginary*no.imaginary
        c = self.real*no.imaginary
        d = self.imaginary*no.real
        return Complex(a-b, c+d)
    def __truediv__(self, no):
        x=complex(self.real, self.imaginary)/complex(no.real, no.imaginary)
        return Complex(x.real, x.imag).__str__()
        
    def mod(self):
        a = self.real
        b = self.imaginary
        return Complex(math.pow(a**2 + b**2, 0.5), 0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
