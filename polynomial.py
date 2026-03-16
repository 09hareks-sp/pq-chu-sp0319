from dataclasses import dataclass

@dataclass
class Polynomial():
    coefficients: list[float] #index 0 is the coefficient of the degree zero term.
    degree: int = 2

    def __str__(self) -> str:
        return_string:str = 'y = '

        ##This should do a lot of coolified things to make this prettier, like
        # - Don't print coeffecients if they're 1
        # - Don't print term if coeffecient is 0
        # - Dynamically change sign (also including not printing leading +)
        for coeffecient, exponent in zip(reversed(self.coefficients), range(self.degree,-1,-1)):
            return_string += f"{coeffecient} * x^{exponent} + "
        return return_string
    
    def value(self: 'Polynomial', x: float) -> float:
        value = 0.0
        x_term = 1
        for coefficient in self.coefficients:
            value += coefficient*x_term
            x_term *= x
        return value

class Poly2(Polynomial):
    def __init__(self,a=1,b=2,c=3):
        with_coefficients=[c,b,a]
        super().__init__(coefficients=with_coefficients)

    @property
    def a(self):
        return self.coefficients[2]
    
    @a.setter
    def a(self, to_value: float):
        self.coefficients[2] = to_value
    
    @property
    def b(self):
        return self.coefficients[1]
    
    @b.setter
    def b(self, to_value: float):
        self.coefficients[1] = to_value
    
    @property
    def c(self):
        return self.coefficients[0]
    
    @c.setter
    def c(self, to_value: float):
        self.coefficients[0] = to_value
    

my_poly = Poly2(1,5,-2)
print(my_poly)

my_poly.b=-2
print(my_poly)