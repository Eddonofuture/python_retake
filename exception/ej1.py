class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("only integers")
        if integer % 2:
            raise ValueError("Only even numbers")
        super().append(integer)


e = EvenOnly()
e.append(2)
#e.append(1)
#e.append("a string")
