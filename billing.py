from person import Person

class Cashier(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def generate_bill(self, patient, amount):
        return f"Cashier {self.name} billed {patient.name} KES {amount}."


class BillingSystem:
    def __init__(self):
        self._records = []   # private: hidden from direct access

    def add_payment(self, patient, amount):
        record = {"patient": patient.name, "amount": amount}
        self._records.append(record)
        return f"Payment recorded for {patient.name}: KES {amount}"

    def show_payments(self):
        return self._records
