from person import Person
from departments import Department

class Pharmacist(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def dispense(self, patient, medicine):
        return f"Pharmacist {self.name} dispensed {medicine} to {patient.name}."


class Pharmacy(Department):
    def __init__(self):
        super().__init__("Pharmacy")
        self.medicine_stock = {}

    def add_medicine(self, name, quantity):
        self.medicine_stock[name] = self.medicine_stock.get(name, 0) + quantity

    def check_stock(self):
        return self.medicine_stock
