"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initialize a start number"""

        self.start = self.next = start

    def __repr__(self):
        """Show representation"""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Increment the start number by 1"""

        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Reset start number to original number"""

        self.next = self.start