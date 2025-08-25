# Python OOP Hospital Management System with Ubuntu Flair! (PRACTISE THIS BY YOUR OWN) 🐍🏥

Hello class! Today we're going to build a hospital management system using Python OOP. Let's dive in with some Ubuntu-inspired fun! 🚀

## Use Case Diagram Overview

```
      +----------------+       +-----------------+       +----------------+
      |    Patient     |       |   MedicalStaff  |       |   Department   |
      +----------------+       +-----------------+       +----------------+
      | - register()   |       | - treat()       |       | - add_staff()  |
      | - check_in()   |       | - diagnose()    |       | - schedule()   |
      | - check_out()  |       | - prescribe()   |       +----------------+
      +----------------+       +-----------------+
            |                          |                       |
            |                          |                       |
      +----------------+       +-----------------+       +----------------+
      |  Appointment   |       |    Treatment    |       |   Billing      |
      +----------------+       +-----------------+       +----------------+
      | - schedule()   |       | - record()      |       | - generate()   |
      | - reschedule() |       | - update()      |       | - process()    |
      +----------------+       +-----------------+       +----------------+
```

Now let's implement this step by step! ⚡

## Step 1: Base Classes (The Foundation)

```python
# Let's start with our base classes - think of these as the 'coreutils' of our hospital!
class Person:
    """Base class for all people in our hospital - like the 'ls' command, it lists all basic info!"""
    
    def __init__(self, name, age, contact_info):
        self.name = name
        self.age = age
        self.contact_info = contact_info
        print(f"🚀 New person created: {self.name} - Ready for hospital adventures!")
    
    def __str__(self):
        return f"{self.name} ({self.age} years) - Contact: {self.contact_info}"

class HospitalEntity:
    """Base class for hospital entities - our 'apt-get' for hospital operations!"""
    
    entity_count = 0  # Class variable - like counting installed packages!
    
    def __init__(self, name):
        self.name = name
        self.id = HospitalEntity.generate_id()
        HospitalEntity.entity_count += 1
    
    @classmethod
    def generate_id(cls):
        """Generate unique ID - like giving each package a unique version number!"""
        return f"HOSP{cls.entity_count:04d}"
    
    @classmethod
    def get_total_entities(cls):
        """Get total entities - similar to 'dpkg --get-selections | wc -l'"""
        return cls.entity_count
```

## Step 2: Patient Class (The Users)

```python
class Patient(Person):
    """Patients are like the 'users' of our hospital system - each with their unique needs!"""
    
    def __init__(self, name, age, contact_info, medical_history=None):
        super().__init__(name, age, contact_info)
        self.patient_id = f"PAT{self.generate_patient_id():04d}"
        self.medical_history = medical_history or []
        self.current_treatment = None
        self.is_admitted = False
        print(f"🎯 Patient {self.patient_id} registered successfully!")
    
    patient_counter = 0
    
    @classmethod
    def generate_patient_id(cls):
        cls.patient_counter += 1
        return cls.patient_counter
    
    def check_in(self, department):
        """Check-in process - like 'ssh' into hospital services!"""
        self.is_admitted = True
        self.current_department = department
        print(f"✅ {self.name} checked into {department.name} department")
        return f"Welcome to {department.name}, {self.name}!"
    
    def check_out(self):
        """Check-out process - like 'exit' from a session!"""
        if self.is_admitted:
            self.is_admitted = False
            print(f"🚪 {self.name} checked out successfully")
            return "Thank you for choosing our hospital!"
        return "Patient was not admitted"
    
    def add_to_medical_history(self, entry):
        """Add medical record - like appending to a log file!"""
        self.medical_history.append(entry)
        print(f"📝 Medical history updated for {self.name}")
    
    def __str__(self):
        status = "Admitted" if self.is_admitted else "Not admitted"
        return f"Patient {self.patient_id}: {super().__str__()} - Status: {status}"
```

## Step 3: Medical Staff Classes (The System Admins)

```python
class MedicalStaff(Person):
    """Medical staff are our 'sudoers' - they have special privileges to treat patients!"""
    
    def __init__(self, name, age, contact_info, staff_type, specialization, license_number):
        super().__init__(name, age, contact_info)
        self.staff_id = f"STAFF{self.generate_staff_id():04d}"
        self.staff_type = staff_type  # Doctor, Nurse, etc.
        self.specialization = specialization
        self.license_number = license_number
        self.current_patients = []
    
    staff_counter = 0
    
    @classmethod
    def generate_staff_id(cls):
        cls.staff_counter += 1
        return cls.staff_counter
    
    def treat_patient(self, patient, treatment_details):
        """Treat a patient - like running a diagnostic tool!"""
        print(f"🩺 {self.name} is treating {patient.name}")
        treatment = Treatment(patient, self, treatment_details)
        patient.add_to_medical_history(treatment)
        self.current_patients.append(patient)
        return treatment
    
    def diagnose(self, patient, diagnosis):
        """Make a diagnosis - similar to analyzing system logs!"""
        print(f"🔍 {self.name} diagnosed {patient.name} with {diagnosis}")
        return f"Diagnosis: {diagnosis}"
    
    def prescribe(self, patient, medication, dosage):
        """Prescribe medication - like recommending software solutions!"""
        prescription = f"Prescribed {medication} ({dosage}) for {patient.name}"
        print(f"💊 {prescription}")
        patient.add_to_medical_history(prescription)
        return prescription

class Doctor(MedicalStaff):
    """Doctors are like 'root' users - they have ultimate treatment authority!"""
    
    def __init__(self, name, age, contact_info, specialization, license_number):
        super().__init__(name, age, contact_info, "Doctor", specialization, license_number)
        print(f"👨‍⚕️ Doctor {self.name} is ready to save lives!")

class Nurse(MedicalStaff):
    """Nurses are our 'systemd' - they keep everything running smoothly!"""
    
    def __init__(self, name, age, contact_info, specialization, license_number):
        super().__init__(name, age, contact_info, "Nurse", specialization, license_number)
        print(f"👩‍⚕️ Nurse {self.name} is on duty and ready to care!")
```

## Step 4: Department Classes (The Services)

```python
class Department(HospitalEntity):
    """Departments are like different 'services' running on our hospital server!"""
    
    def __init__(self, name, department_type):
        super().__init__(name)
        self.department_type = department_type
        self.staff_members = []
        self.patients = []
        self.equipment = []
        print(f"🏥 {self.department_type} Department '{self.name}' initialized!")
    
    def add_staff(self, staff_member):
        """Add staff to department - like adding users to a group!"""
        if staff_member not in self.staff_members:
            self.staff_members.append(staff_member)
            print(f"➕ Added {staff_member.name} to {self.name} department")
        return self.staff_members
    
    def admit_patient(self, patient):
        """Admit patient - similar to granting access to a service!"""
        if patient not in self.patients:
            self.patients.append(patient)
            patient.check_in(self)
            print(f"📋 Patient {patient.name} admitted to {self.name}")
        return self.patients
    
    def discharge_patient(self, patient):
        """Discharge patient - like revoking service access!"""
        if patient in self.patients:
            self.patients.remove(patient)
            patient.check_out()
            print(f"📤 Patient {patient.name} discharged from {self.name}")
        return self.patients
    
    def schedule_appointment(self, patient, doctor, time_slot):
        """Schedule appointment - like cron job scheduling!"""
        appointment = Appointment(patient, doctor, self, time_slot)
        print(f"📅 Appointment scheduled: {patient.name} with Dr. {doctor.name} at {time_slot}")
        return appointment
    
    def get_stats(self):
        """Get department stats - similar to 'systemctl status'!"""
        return {
            'department': self.name,
            'type': self.department_type,
            'staff_count': len(self.staff_members),
            'patient_count': len(self.patients),
            'equipment_count': len(self.equipment)
        }

class EmergencyDepartment(Department):
    """Emergency Department - our hospital's 'emergency mode' or 'recovery mode'!"""
    
    def __init__(self, name):
        super().__init__(name, "Emergency")
        self.emergency_cases = []
        print("🚨 Emergency Department activated! Ready for critical cases!")
    
    def handle_emergency(self, patient, emergency_type):
        """Handle emergency - like responding to system critical alerts!"""
        print(f"🚑 EMERGENCY: {patient.name} with {emergency_type}")
        self.emergency_cases.append({
            'patient': patient,
            'type': emergency_type,
            'timestamp': 'NOW',
            'status': 'In Progress'
        })
        return f"Emergency case registered for {patient.name}"

class SurgeryDepartment(Department):
    """Surgery Department - where we perform 'system surgeries'!"""
    
    def __init__(self, name):
        super().__init__(name, "Surgery")
        self.operating_rooms = []
        self.scheduled_surgeries = []
        print("🔪 Surgery Department ready for operations!")
    
    def schedule_surgery(self, patient, surgeon, surgery_type, time_slot):
        """Schedule surgery - like planning a major system update!"""
        surgery = {
            'patient': patient,
            'surgeon': surgeon,
            'type': surgery_type,
            'time': time_slot,
            'status': 'Scheduled'
        }
        self.scheduled_surgeries.append(surgery)
        print(f"🩺 Surgery scheduled: {surgery_type} for {patient.name} by Dr. {surgeon.name}")
        return surgery
```

## Step 5: Supporting Classes (The Utilities)

```python
class Treatment:
    """Treatment class - records medical interventions like system logs!"""
    
    def __init__(self, patient, medical_staff, details):
        self.patient = patient
        self.medical_staff = medical_staff
        self.details = details
        self.timestamp = "NOW"
        self.treatment_id = f"TREAT{hash(self)}"[:10]
    
    def __str__(self):
        return f"Treatment {self.treatment_id}: {self.details} by {self.medical_staff.name}"

class Appointment:
    """Appointment class - manages patient-doctor meetings like calendar events!"""
    
    def __init__(self, patient, doctor, department, time_slot):
        self.patient = patient
        self.doctor = doctor
        self.department = department
        self.time_slot = time_slot
        self.status = "Scheduled"
        self.appointment_id = f"APT{hash(self)}"[:8]
        print(f"📋 Appointment {self.appointment_id} created successfully!")
    
    def reschedule(self, new_time_slot):
        """Reschedule appointment - like modifying cron jobs!"""
        old_time = self.time_slot
        self.time_slot = new_time_slot
        print(f"⏰ Appointment rescheduled from {old_time} to {new_time_slot}")
        return self
    
    def complete(self):
        """Mark appointment as complete - like checking off a todo item!"""
        self.status = "Completed"
        print(f"✅ Appointment {self.appointment_id} marked as completed")
        return self
    
    def __str__(self):
        return f"Appointment {self.appointment_id}: {self.patient.name} with Dr. {self.doctor.name} at {self.time_slot}"

class Billing:
    """Billing class - handles financial transactions like package management costs!"""
    
    def __init__(self):
        self.invoices = []
        print("💰 Billing system initialized! Ready for financial operations!")
    
    def generate_invoice(self, patient, services, total_amount):
        """Generate invoice - like creating a billing statement!"""
        invoice = {
            'patient': patient,
            'services': services,
            'amount': total_amount,
            'status': 'Generated',
            'invoice_id': f"INV{len(self.invoices) + 1:04d}"
        }
        self.invoices.append(invoice)
        print(f"🧾 Invoice {invoice['invoice_id']} generated for {patient.name}: ${total_amount}")
        return invoice
    
    def process_payment(self, invoice_id, payment_method):
        """Process payment - like completing a transaction!"""
        for invoice in self.invoices:
            if invoice['invoice_id'] == invoice_id:
                invoice['status'] = 'Paid'
                invoice['payment_method'] = payment_method
                print(f"💳 Payment processed for invoice {invoice_id} via {payment_method}")
                return invoice
        return "Invoice not found"
```

## Step 6: Hospital System (The Main Server)

```python
class HospitalSystem:
    """Main Hospital System - our Ubuntu server managing all operations!"""
    
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.patients = []
        self.staff = []
        self.billing_system = Billing()
        print(f"🎉 {self.name} Hospital System booted up successfully!")
        print("=" * 60)
        print("🏥 WELCOME TO UBUNTU HOSPITAL MANAGEMENT SYSTEM!")
        print("🐧 Where we treat patients with open-source care!")
        print("=" * 60)
    
    def add_department(self, department):
        """Add department - like enabling a new system service!"""
        self.departments.append(department)
        print(f"➕ Department added: {department.name}")
        return self.departments
    
    def register_patient(self, name, age, contact_info):
        """Register patient - like adding a new user account!"""
        patient = Patient(name, age, contact_info)
        self.patients.append(patient)
        return patient
    
    def hire_staff(self, staff_type, *args, **kwargs):
        """Hire staff - like installing new system packages!"""
        if staff_type.lower() == 'doctor':
            staff = Doctor(*args, **kwargs)
        elif staff_type.lower() == 'nurse':
            staff = Nurse(*args, **kwargs)
        else:
            staff = MedicalStaff(*args, **kwargs)
        
        self.staff.append(staff)
        print(f"👥 New staff hired: {staff.name} ({staff.staff_type})")
        return staff
    
    def get_stats(self):
        """Get system statistics - like 'top' or 'htop' for hospital!"""
        return {
            'hospital_name': self.name,
            'total_departments': len(self.departments),
            'total_patients': len(self.patients),
            'total_staff': len(self.staff),
            'total_entities': HospitalEntity.get_total_entities()
        }
    
    def emergency_alert(self, patient, emergency_type):
        """Emergency alert system - like critical system notifications!"""
        print(f"🚨🚨🚨 EMERGENCY ALERT! 🚨🚨🚨")
        print(f"Patient: {patient.name}")
        print(f"Emergency: {emergency_type}")
        print(f"Directing to Emergency Department...")
        
        # Find emergency department
        for dept in self.departments:
            if isinstance(dept, EmergencyDepartment):
                return dept.handle_emergency(patient, emergency_type)
        
        return "No emergency department found!"
```

## Step 7: Let's Test Our Hospital System! 🧪

```python
def demonstrate_hospital_system():
    """Demo function - let's see our hospital in action!"""
    
    print("\n" + "="*60)
    print("🚀 STARTING UBUNTU HOSPITAL DEMONSTRATION!")
    print("="*60)
    
    # Initialize our hospital - like booting up Ubuntu!
    ubuntu_hospital = HospitalSystem("Ubuntu Medical Center")
    
    # Create departments - enabling our services!
    emergency_dept = EmergencyDepartment("Emergency Care")
    surgery_dept = SurgeryDepartment("Advanced Surgery")
    cardiology_dept = Department("Heart Care", "Cardiology")
    
    ubuntu_hospital.add_department(emergency_dept)
    ubuntu_hospital.add_department(surgery_dept)
    ubuntu_hospital.add_department(cardiology_dept)
    
    # Hire medical staff - installing our expert packages!
    dr_smith = ubuntu_hospital.hire_staff(
        'doctor', "Dr. Smith", 45, "555-1234", 
        "Cardiology", "MD12345"
    )
    
    nurse_jones = ubuntu_hospital.hire_staff(
        'nurse', "Nurse Jones", 32, "555-5678",
        "Emergency Care", "RN67890"
    )
    
    # Add staff to departments - assigning permissions!
    cardiology_dept.add_staff(dr_smith)
    emergency_dept.add_staff(nurse_jones)
    
    # Register patients - creating user accounts!
    patient_john = ubuntu_hospital.register_patient("John Doe", 30, "john@email.com")
    patient_sarah = ubuntu_hospital.register_patient("Sarah Smith", 25, "sarah@email.com")
    
    # Demonstrate patient flow
    print("\n--- PATIENT JOURNEY ---")
    cardiology_dept.admit_patient(patient_john)
    
    # Schedule appointment - like setting up a meeting!
    appointment = cardiology_dept.schedule_appointment(
        patient_john, dr_smith, "2024-01-15 10:00 AM"
    )
    
    # Doctor treats patient - providing care!
    treatment = dr_smith.treat_patient(patient_john, "Routine heart checkup")
    diagnosis = dr_smith.diagnose(patient_john, "Healthy heart")
    prescription = dr_smith.prescribe(patient_john, "Aspirin", "81mg daily")
    
    # Emergency situation!
    print("\n--- EMERGENCY SCENARIO ---")
    ubuntu_hospital.emergency_alert(patient_sarah, "Severe allergic reaction")
    emergency_dept.admit_patient(patient_sarah)
    
    # Generate billing - financial operations!
    print("\n--- BILLING OPERATIONS ---")
    invoice = ubuntu_hospital.billing_system.generate_invoice(
        patient_john, 
        ["Consultation", "Medication"], 
        250.00
    )
    
    payment = ubuntu_hospital.billing_system.process_payment(
        invoice['invoice_id'], "Credit Card"
    )
    
    # Show statistics - system monitoring!
    print("\n--- HOSPITAL STATISTICS ---")
    stats = ubuntu_hospital.get_stats()
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print("\n" + "="*60)
    print("🎉 DEMONSTRATION COMPLETE! UBUNTU HOSPITAL IS OPERATIONAL!")
    print("="*60)

# Run the demonstration
if __name__ == "__main__":
    demonstrate_hospital_system()
```

## Key OOP Concepts Demonstrated: 🎯

1. **Inheritance**: `Patient` and `MedicalStaff` inherit from `Person`
2. **Encapsulation**: Private attributes with getter/setter methods
3. **Polymorphism**: Different department types with specialized methods
4. **Abstraction**: Complex operations hidden behind simple interfaces
5. **Class Methods**: For generating IDs and tracking counts
6. **Composition**: Hospital contains departments, which contain staff and patients

## Ubuntu-inspired Features: 🐧

- **Modular Design**: Like Ubuntu packages, each class has a specific purpose
- **System Monitoring**: Statistics tracking like system resource monitoring
- **User Management**: Patient registration like user account creation
- **Service Management**: Departments function like system services
- **Logging**: Medical history acts as system logs

This implementation provides a solid foundation that can be extended with databases, GUIs, or web interfaces! Remember: good OOP design is like a well-maintained Ubuntu system - modular, scalable, and easy to maintain! 💻🏥
