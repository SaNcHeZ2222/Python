class ComplexNumber:
    def __init__(self, body):
        self.body = body

    def __add__(self, other):
        one = (complex(self.body))
        two = (complex(other.body))
        print(one+two)

    def __mul__(self, other):
        one = (complex(self.body))
        two = (complex(other.body))
        print(one*two)

one = ComplexNumber('2+j')
two = ComplexNumber('3+4j')

one+two
print()
one*two