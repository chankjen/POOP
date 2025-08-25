class Person:
    def __init__(self, name, age):
        self.name = name        # Public attribute
        self._age = age         # Protected (convention: starts with _)
    
    def get_details(self):
        return f"{self.name}, Age: {self._age}"
