class Value:
    def __init__(self, value, children=set(), operation=''):
        self.value = value
        self.gradient = 0 # initial gradient is zero
        self.operation = operation
        self.children = children
        self.label = str(value)

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.value+other.value, (self,other), '+')

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.value*other.value, (self,other), '*')

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "can only raise to int or float power"
        return Value(self.value**other, (self,), f'**{other}')

    def relu(self):
        return Value(0 if self.value < 0 else self.value, (self,), 'ReLU')

    def __neg__(self): # -self
        return self * -1

    def __radd__(self, other): # other + self
        return self + other

    def __sub__(self, other): # self - other
        return self + (-other)

    def __rsub__(self, other): # other - self
        return other + (-self)

    def __rmul__(self, other): # other * self
        return self * other

    def __truediv__(self, other): # self / other
        return self * other**-1

    def __rtruediv__(self, other): # other / self
        return other * self**-1

    def __repr__(self):
        return f"Value(value={self.value}, gradient={self.gradient})"
