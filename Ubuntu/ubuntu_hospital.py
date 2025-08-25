#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ubuntu Hospital Management System
Coding with the spirit of open source healing!
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Optional
import random

# Let's start with our base classes
class Person(ABC):
    """Base class for all people in our hospital system"""
    
    def __init__(self, name: str, id: str, contact: str):
        self._name = name  # Encapsulation in action!
        self._id = id
        self._contact = contact
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def id(self) -> str:
        return self._id
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self._name} (ID: {self._id})"
    
    @abstractmethod
    def perform_duties(self):
        """Abstract method - each person has different duties"""
        pass


class Patient(Person):
    """Patient class - the reason we're here!"""
    
    def __init__(self, name: str, id: str, contact: str, medical_history: str = ""):
        super().__init__(name, id, contact)
        self._medical_history = medical_history
        self._current_treatment = None
        self._assigned_doctor = None
        self._admission_date = datetime.now()
        print(f"🖥️  Patient {name} admitted to Ubuntu Hospital at {self._admission_date}")
    
    def assign_doctor(self, doctor):
        self._assigned_doctor = doctor
        print(f"🖥️  Dr. {doctor.name} assigned to patient {self.name}")
    
    def assign_treatment(self, treatment):
        self._current_treatment = treatment
        print(f"🖥️  Treatment '{treatment}' assigned to patient {self.name}")
    
    def perform_duties(self):
        # Patients don't perform duties, they receive care
        print(f"🖥️  Patient {self.name} is resting and recovering")
    
    def discharge(self):
        print(f"🖥️  Patient {self.name} discharged from Ubuntu Hospital. Get well soon!")
        return f"Discharge summary for {self.name}"


class MedicalStaff(Person):
    """Base class for all medical staff"""
    
    def __init__(self, name: str, id: str, contact: str, department: str, license_num: str):
        super().__init__(name, id, contact)
        self._department = department
        self._license_num = license_num
        self._patients = []
    
    def assign_patient(self, patient: Patient):
        self._patients.append(patient)
        patient.assign_doctor(self)
        print(f"🖥️  {self.__class__.__name__} {self.name} assigned to patient {patient.name}")
    
    @abstractmethod
    def provide_treatment(self, patient: Patient, treatment: str):
        pass


# Let's create specific medical staff types using inheritance
class Doctor(MedicalStaff):
    """Doctor class - specialized medical staff"""
    
    def __init__(self, name: str, id: str, contact: str, department: str, 
                 license_num: str, specialty: str):
        super().__init__(name, id, contact, department, license_num)
        self._specialty = specialty
        print(f"🖥️  Dr. {name} ({specialty}) joined Ubuntu Hospital")
    
    def provide_treatment(self, patient: Patient, treatment: str):
        print(f"🖥️  Dr. {self.name} is providing {treatment} to patient {patient.name}")
        patient.assign_treatment(treatment)
        return f"Treatment provided: {treatment}"
    
    def perform_surgery(self, patient: Patient, surgery_type: str):
        print(f"🖥️  Dr. {self.name} is performing {surgery_type} on {patient.name}")
        return f"Surgery completed: {surgery_type}"
    
    def perform_duties(self):
        print(f"🖥️  Dr. {self.name} is making rounds in the {self._department} department")


class Nurse(MedicalStaff):
    """Nurse class - essential care providers"""
    
    def __init__(self, name: str, id: str, contact: str, department: str, 
                 license_num: str, shift: str):
        super().__init__(name, id, contact, department, license_num)
        self._shift = shift
        print(f"🖥️  Nurse {name} ({shift} shift) joined Ubuntu Hospital")
    
    def provide_treatment(self, patient: Patient, treatment: str):
        print(f"🖥️  Nurse {self.name} is administering {treatment} to patient {patient.name}")
        return f"Treatment administered: {treatment}"
    
    def monitor_patient(self, patient: Patient):
        print(f"🖥️  Nurse {self.name} is monitoring patient {patient.name}")
        return f"Patient vitals: Stable"
    
    def perform_duties(self):
        print(f"🖥️  Nurse {self.name} is providing care during the {self._shift} shift")


# Let's create our hospital departments
class Department(ABC):
    """Abstract base class for hospital departments"""
    
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._staff = []
        self._equipment = []
        print(f"🖥️  {name} department initialized at {location}")
    
    def add_staff(self, staff: MedicalStaff):
        self._staff.append(staff)
        print(f"🖥️  {staff.name} added to {self._name} department")
    
    def add_equipment(self, equipment: str):
        self._equipment.append(equipment)
        print(f"🖥️  {equipment} added to {self._name} department")
    
    @abstractmethod
    def department_operation(self):
        pass
    
    def __str__(self):
        return f"{self._name} Department at {self._location}"


# Concrete department implementations
class EmergencyDepartment(Department):
    """Emergency Department - handles urgent cases"""
    
    def __init__(self, location: str):
        super().__init__("Emergency", location)
        self._triage_levels = ["Immediate", "Very Urgent", "Urgent", "Less Urgent", "Non-Urgent"]
    
    def triage_patient(self, patient: Patient, severity: int) -> str:
        level = self._triage_levels[severity - 1] if 1 <= severity <= 5 else "Unknown"
        print(f"🖥️  Patient {patient.name} triaged as {level} priority")
        return level
    
    def department_operation(self):
        print(f"🖥️  Emergency Department operating: Providing urgent care 24/7")
        return "Emergency services available"


class CardiologyDepartment(Department):
    """Cardiology Department - heart specialists"""
    
    def __init__(self, location: str):
        super().__init__("Cardiology", location)
        self._special_equipment = ["EKG Machine", "Echocardiogram", "Stress Test System"]
    
    def perform_ecg(self, patient: Patient):
        print(f"🖥️  Performing ECG on patient {patient.name} in Cardiology")
        return "ECG results: Normal sinus rhythm"
    
    def department_operation(self):
        print(f"🖥️  Cardiology Department operating: Heart health is our specialty")
        return "Cardiac care services available"


# The main hospital system
class UbuntuHospital:
    """Our main hospital system - where everything comes together!"""
    
    def __init__(self, name: str):
        self._name = name
        self._departments = {}
        self._patients = {}
        self._staff = {}
        print(f"🖥️  === {name} === Initialized! === ")
        print(f"🖥️  Welcome to Ubuntu Hospital - Open Source Healing!")
        print(f"🖥️  Type 'hospital.help()' for available operations\n")
    
    def add_department(self, department: Department):
        self._departments[department._name] = department
        print(f"🖥️  Added {department._name} to Ubuntu Hospital")
    
    def admit_patient(self, name: str, contact: str, medical_history: str = "") -> Patient:
        patient_id = f"PAT{random.randint(1000, 9999)}"
        patient = Patient(name, patient_id, contact, medical_history)
        self._patients[patient_id] = patient
        return patient
    
    def hire_staff(self, staff_type: str, **kwargs) -> MedicalStaff:
        staff_id = f"{staff_type.upper()[0]}{random.randint(100, 999)}"
        
        if staff_type.lower() == "doctor":
            staff = Doctor(**kwargs, id=staff_id)
        elif staff_type.lower() == "nurse":
            staff = Nurse(**kwargs, id=staff_id)
        else:
            raise ValueError(f"Unknown staff type: {staff_type}")
        
        self._staff[staff_id] = staff
        return staff
    
    def assign_patient_to_doctor(self, patient_id: str, doctor_id: str):
        patient = self._patients.get(patient_id)
        doctor = self._staff.get(doctor_id)
        
        if patient and doctor and isinstance(doctor, Doctor):
            doctor.assign_patient(patient)
        else:
            print("🖥️  Assignment failed. Check patient and doctor IDs.")
    
    def simulate_day(self):
        print(f"\n🖥️  === Simulation of a day at Ubuntu Hospital ===\n")
        
        # Departments operate
        for dept_name, dept in self._departments.items():
            dept.department_operation()
        
        # Staff perform duties
        for staff_id, staff in self._staff.items():
            staff.perform_duties()
        
        # Patients receive care
        for patient_id, patient in self._patients.items():
            patient.perform_duties()
        
        print(f"\n🖥️  === End of day simulation ===\n")
    
    def help(self):
        print(f"\n🖥️  === Ubuntu Hospital Management System Help ===")
        print(f"🖥️  Available operations:")
        print(f"🖥️  - hospital.add_department(department)")
        print(f"🖥️  - hospital.admit_patient(name, contact, medical_history)")
        print(f"🖥️  - hospital.hire_staff(staff_type, **kwargs)")
        print(f"🖥️  - hospital.assign_patient_to_doctor(patient_id, doctor_id)")
        print(f"🖥️  - hospital.simulate_day()")
        print(f"🖥️  - hospital.help()")
        print(f"🖥️  =============================================\n")


# Let's put it all together in a demonstration
if __name__ == "__main__":
    print("🚀 Launching Ubuntu Hospital Management System...\n")
    
    # Initialize our hospital
    hospital = UbuntuHospital("Ubuntu Community Hospital")
    
    # Add departments
    emergency = EmergencyDepartment("Ground Floor, West Wing")
    cardiology = CardiologyDepartment("First Floor, East Wing")
    
    hospital.add_department(emergency)
    hospital.add_department(cardiology)
    
    # Hire staff
    dr_smith = hospital.hire_staff("doctor", 
                                 name="Sarah Smith", 
                                 contact="s.smith@ubuntu-hospital.com",
                                 department="Cardiology",
                                 license_num="MD123456",
                                 specialty="Cardiologist")
    
    nurse_jones = hospital.hire_staff("nurse",
                                    name="Robert Jones",
                                    contact="r.jones@ubuntu-hospital.com",
                                    department="Emergency",
                                    license_num="RN654321",
                                    shift="Day")
    
    # Admit patients
    patient1 = hospital.admit_patient("John Doe", "555-1234", "Hypertension")
    patient2 = hospital.admit_patient("Jane Smith", "555-5678", " Chest pain")
    
    # Assign staff to departments
    cardiology.add_staff(dr_smith)
    emergency.add_staff(nurse_jones)
    
    # Assign patients to doctors
    hospital.assign_patient_to_doctor(patient1.id, dr_smith.id)
    
    # Provide some treatment
    dr_smith.provide_treatment(patient1, "Medication adjustment")
    nurse_jones.monitor_patient(patient2)
    
    # Triage a patient
    emergency.triage_patient(patient2, 2)
    
    # Perform specialized procedures
    cardiology.perform_ecg(patient1)
    
    # Simulate a day at the hospital
    hospital.simulate_day()
    
    # Demonstrate polymorphism
    print("🖥️  === Polymorphism in Action ===")
    people = [patient1, dr_smith, nurse_jones]
    for person in people:
        person.perform_duties()
    
    # Discharge a patient
    patient1.discharge()
    
    print(f"\n✨ Ubuntu Hospital demonstration complete!")
    print(f"✨ Remember: In coding and healthcare, collaboration is key!")