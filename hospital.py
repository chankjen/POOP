from billing import BillingSystem

class Hospital:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.patients = []
        self.billing_system = BillingSystem()
    
    def add_department(self, department):
        self.departments.append(department)
    
    def admit_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} admitted with {patient.ailment}.")

    def show_departments(self):
        return [dept.name for dept in self.departments]

