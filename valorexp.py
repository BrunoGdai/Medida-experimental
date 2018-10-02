from math import log

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

    def __sub__(self, other):
        if isinstance(other, ValorExp):
            return ValorExp(self.val - other.val, self.inc + other.inc)
        else:
            return ValorExp(self.val - other, self.inc)

    def __mul__(self, other):
        if isinstance(other, ValorExp):
            return ValorExp(self.val * other.val, self.inc * other.val + self.val * other.inc)
        else:
            return ValorExp(self.val * other, self.inc * other)

    def __pow__(self, n):  # n é real
        return ValorExp(self.val**n, n * self.val ** (n - 1) * self.inc)

    def __truediv__(self, other):
        if isinstance(other, ValorExp):
            return ValorExp(self.val / other.val, (self.inc * other.val + self.val * other.inc) / other.val ** 2)
        else:
            return ValorExp(self.val / other, self.inc / other)

    def __rtruediv__(self, other):
        return ValorExp(other / self.val, self.inc * (1 / other))

    def __radd__(self, other):
        return ValorExp(other + self.val, self.inc)

    def __rsub__(self, other):
        return ValorExp(other - self.val, self.inc)

    def __rpow__(self, other):
        return ValorExp(other ** self.val, other ** self.val * log(other) * self.inc)

    def __rmul__(self, other):
        return ValorExp(self.val * other, self.inc * other)

    def __repr__(self):
        return str(self.val) + ' ± ' + str(self.inc)
