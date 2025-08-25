from hospital import Hospital
from doctor import Doctor, Patient
from departments import Cardiology, Pediatrics
from pharmacist import Pharmacy, Pharmacist
from billing import Cashier


# Create Hospital
hospital = Hospital("Ubuntu Community Hospital")

# Create Departments
cardiology = Cardiology()
pediatrics = Pediatrics()
pharmacy = Pharmacy()
hospital.add_department(cardiology)
hospital.add_department(pediatrics)
hospital.add_department(pharmacy)

# Create Doctors
doc_mary = Doctor("Mary Achieng", 45, "Cardiology")
doc_kamau = Doctor("Kamau Mwangi", 38, "Pediatrics")

# Add Doctors to Departments
cardiology.add_doctor(doc_mary)
pediatrics.add_doctor(doc_kamau)

# Pharmacist
pharmacist = Pharmacist("Alice Wambui", 32)

# Cashier
cashier = Cashier("Peter Njoroge", 40)


# Admit Patients
patient_john = Patient("John Otieno", 30, "Chest Pain")
patient_anne = Patient("Anne Njeri", 5, "Fever")
hospital.admit_patient(patient_john)
hospital.admit_patient(patient_anne)

# Doctor treats patient
print(doc_mary.treat(patient_john))
print(doc_kamau.treat(patient_anne))

# Show Hospital Info
print("\nDepartments:", hospital.show_departments())
print("Cardiology Doctors:", cardiology.get_doctors())
print("Pediatrics Doctors:", pediatrics.get_doctors())

# Pharmacy actions
pharmacy.add_medicine("Paracetamol", 50)
print(pharmacist.dispense(patient_anne, "Paracetamol"))
print("Pharmacy Stock:", pharmacy.check_stock())

# Billing actions
print(cashier.generate_bill(patient_john, 1500))
print(hospital.billing_system.add_payment(patient_john, 1500))
print(hospital.billing_system.show_payments())
