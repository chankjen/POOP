from person import Person

class Doctor(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty
    
    def treat(self, patient):
        return f"Dr. {self.name} is treating {patient.name} for {patient.ailment} in {self.specialty}."

class Patient(Person):
    def __init__(self, name, age, ailment):
        super().__init__(name, age)
        self.ailment = ailment
