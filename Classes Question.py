class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    # This method allows the object to be iterable
    def __iter__(self):
        # We yield first the length and then the width in the required format
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rectangle = Rectangle(5, 10)

# Iterating over the rectangle object
for dimension in rectangle:
    print(dimension)
