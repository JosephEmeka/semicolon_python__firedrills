class Complex:
    def _init_(self, left, right):
        self.left = left
        self.right = right

    def _add_(self, other):
        return complex(self.left + other.left and self.right + other.right)

    def _sub_(self, other):
        return complex(self.left - other.left and self.right - other.right)

    def _eq_(self, other):
        return self.left == other.left and self.right == other.right

    def _gt_(self, other):
        return self.left > other.left and self.right > other.right

    def _repr_(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i'

    def __iadd__(self, other):
        self.left += other.left
        self.right += other.right
        return complex(self.left, self.right)


c1 = complex(2, 3)
c2 = complex(5, -2)
c3 = complex(2, 3)
print(c1)
print(c2)
print(c1 - c2)
print(c1 == c2)
print(c1 != c3)
c1 += c2
print(c1)
