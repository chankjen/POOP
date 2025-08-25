class Department:
    def __init__(self, name):
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    
    def get_doctors(self):
        return [doc.name for doc in self.doctors]

class Cardiology(Department):
    def __init__(self):
        super().__init__("Cardiology")

class Pediatrics(Department):
    def __init__(self):
        super().__init__("Pediatrics")
