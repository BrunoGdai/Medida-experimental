class ValorExp:
    def __init__(self, val, inc):
        self.val = val  # valor medido
        self.inc = inc  # incerteza

    def __neg__(self):
        return ValorExp(-self.val, self.inc)

    def __add__(self, other):
        if isinstance(other, ValorExp):
            return ValorExp(self.val + other.val, self.inc + other.inc)
        else:
            return ValorExp(self.val + other, self.inc)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, ValorExp):
            return ValorExp(self.val - other.val, self.inc + other.inc)
        else:
            return ValorExp(self.val - other, self.inc)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, ValorExp):
            return ValorExp(self.val * other.val, self.inc * other.val + self.val * other.inc)
        else:
            return ValorExp(self.val * other, self.inc * other)

    __rmul__ = __mul__

    def __pow__(self, n):  # n é real
        return ValorExp(self.val**n, n * self.val ** (n - 1) * self.inc)

    def __truediv__(self, other):
        if isinstance(other, ValorExp):
            if other.val == 0:
                raise ZeroDivisionError
            else:
                return ValorExp(self.val / other.val, (self.inc * other.val + self.val * other.inc) / other.val ** 2)
        else:
            if other == 0:
                raise ZeroDivisionError
            else:
                return ValorExp(self.val / other, self.inc / other)

    def __rtruediv__(self, other):
        return other.__mul__(self.__pow__(-1))

    def __repr__(self):
        return str(self.val) + ' ± ' + str(self.inc)
